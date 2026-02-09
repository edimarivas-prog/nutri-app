import streamlit as st
import pandas as pd
from recetas import RECETARIO # Importamos tu base de datos

# --- CONFIGURACIÓN DE LA PÁGINA (Estilo App Móvil) ---
st.set_page_config(
    page_title="NutriApp Ven-Per",
    page_icon="🥑",
    layout="centered"
)

# --- 1. BARRA LATERAL: DATOS BIOMÉTRICOS ---
st.sidebar.header("⚙️ Configuración Personal")
st.sidebar.write("Actualiza tu peso aquí cada semana.")

# Pesos Base (Punto de partida enero 2026)
BASE_EDIMAR = 102.0
BASE_CARLOS = 81.0

# Entradas de usuario
peso_edimar = st.sidebar.number_input("Peso Edimar (kg):", value=102.0, step=0.5)
peso_carlos = st.sidebar.number_input("Peso Carlos (kg):", value=81.0, step=0.5)

# --- 2. MOTOR DE CÁLCULO (EL ALGORITMO) ---
def calcular_factor(peso_actual, peso_base):
    # Si bajan de peso, las porciones bajan proporcionalmente para seguir perdiendo
    # Si el peso es igual al base, el factor es 1.0
    return peso_actual / peso_base

factor_e = calcular_factor(peso_edimar, BASE_EDIMAR)
factor_c = calcular_factor(peso_carlos, BASE_CARLOS)

# --- 3. INTERFAZ PRINCIPAL ---
st.title("🥑 Planificador Semanal")
st.write(f"**Objetivo:** Déficit calórico activo.")

# Pestañas para organizar la vista en celular
tab1, tab2, tab3 = st.tabs(["📅 Menú", "🥣 Porciones", "🛒 Lista de Compras"])

with tab1:
    st.header("Diseña tu Semana")
    
    # Selectores de Recetas
    desayuno_sel = st.selectbox("🍳 Desayunos (Carlos):", [r['nombre'] for r in RECETARIO['Desayunos']])
    
    st.subheader("🍛 Almuerzos (Batch Cooking)")
    col1, col2 = st.columns(2)
    with col1:
        almuerzo_a_sel = st.selectbox("Lote A (Lun-Mar-Mié):", [r['nombre'] for r in RECETARIO['Almuerzos']], index=0)
    with col2:
        almuerzo_b_sel = st.selectbox("Lote B (Jue-Vie):", [r['nombre'] for r in RECETARIO['Almuerzos']], index=1)
        
    cena_sel = st.selectbox("🌙 Cenas (Edimar):", [r['nombre'] for r in RECETARIO['Cenas']])

with tab2:
    st.header("Tus Cantidades Exactas")
    
    def mostrar_detalle(titulo, receta_nombre, categoria, factor, usuario):
        # Buscar la receta completa en la base de datos
        receta = next(r for r in RECETARIO[categoria] if r['nombre'] == receta_nombre)
        
        with st.expander(f"{titulo}: {receta_nombre} ({usuario})"):
            st.write(f"_{receta['descripcion']}_")
            for ing in receta['ingredientes']:
                # LA MAGIA: Ajuste dinámico
                cantidad_ajustada = round(ing['cantidad'] * factor)
                st.write(f"- **{ing['item']}**: {cantidad_ajustada} {ing['unidad']}")
            st.caption(f"📝 {receta.get('instrucciones', '')}")

    st.subheader("👩 Para Edimar")
    mostrar_detalle("Desayuno", desayuno_sel, "Desayunos", factor_e, "Edimar")
    mostrar_detalle("Almuerzo A", almuerzo_a_sel, "Almuerzos", factor_e, "Edimar")
    mostrar_detalle("Cena", cena_sel, "Cenas", factor_e, "Edimar")

    st.subheader("👨 Para Carlos")
    mostrar_detalle("Desayuno", desayuno_sel, "Desayunos", factor_c, "Carlos")
    mostrar_detalle("Almuerzo B", almuerzo_b_sel, "Almuerzos", factor_c, "Carlos")
    mostrar_detalle("Cena", cena_sel, "Cenas", factor_c, "Carlos")

with tab3:
    st.header("🛒 Lista de Supermercado")
    st.caption("Calculada para: 5 días de Desayuno/Cena + 3 días Almuerzo A + 2 días Almuerzo B")
    
    if st.button("Generar Lista de Compras"):
        lista_compras = {}

        def agregar_a_lista(receta_nombre, categoria, dias, personas_factor_sum):
            receta = next(r for r in RECETARIO[categoria] if r['nombre'] == receta_nombre)
            for ing in receta['ingredientes']:
                # Fórmula: Cantidad Base * (Factor Edimar + Factor Carlos) * Días
                total = ing['cantidad'] * personas_factor_sum * dias
                item = ing['item']
                if item in lista_compras:
                    lista_compras[item] += total
                else:
                    lista_compras[item] = total

        # Lógica de días (Lunes a Viernes)
        # Asumimos que ambos comen lo mismo en desayuno y cena los 5 días
        agregar_a_lista(desayuno_sel, "Desayunos", 5, factor_e + factor_c)
        agregar_a_lista(cena_sel, "Cenas", 5, factor_e + factor_c)
        
        # Almuerzos divididos
        agregar_a_lista(almuerzo_a_sel, "Almuerzos", 3, factor_e + factor_c) # Lun-Mie
        agregar_a_lista(almuerzo_b_sel, "Almuerzos", 2, factor_e + factor_c) # Jue-Vie

        # Mostrar lista limpia
        df = pd.DataFrame(list(lista_compras.items()), columns=['Producto', 'Cantidad Total'])
        df['Cantidad Total'] = df['Cantidad Total'].apply(lambda x: f"{x:.0f}")
        st.dataframe(df, use_container_width=True)
        
        st.success("¡Lista generada! Captura esta pantalla y ve al mercado.")
