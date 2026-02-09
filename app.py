import streamlit as st
import pandas as pd
from recetas import RECETARIO

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="NutriApp Ven-Per", page_icon="🥑", layout="wide")

# --- BARRA LATERAL (DATOS) ---
st.sidebar.header("⚙️ Tus Datos")

# DATOS EDIMAR
peso_edimar = st.sidebar.number_input(
    "Peso Edimar (kg)", 
    min_value=60.0, 
    max_value=150.0, 
    value=102.0, 
    step=0.5
)

# DATOS CARLOS
peso_carlos = st.sidebar.number_input(
    "Peso Carlos (kg)", 
    min_value=60.0, 
    max_value=150.0, 
    value=81.0, 
    step=0.5
)

# Factores de ajuste (Base aproximada 2000kcal)
factor_e = peso_edimar / 102.0
factor_c = peso_carlos / 81.0

st.title("🥑 Planificador Semanal")

# --- PESTAÑAS PRINCIPALES ---
tab_plan, tab_cocina, tab_recetario = st.tabs(["📋 Planificador", "🍳 Cocina y Porciones", "📖 Recetario Paso a Paso"])

# ==========================================
# 1. PESTAÑA: PLANIFICADOR (DOMINGO)
# ==========================================
with tab_plan:
    st.markdown("### 1. Elige tus Almuerzos (Batch Cooking)")
    col1, col2 = st.columns(2)
    with col1:
        almuerzo_3_dias = st.selectbox("Almuerzo Largo (Para 3 días):", [r['nombre'] for r in RECETARIO['Almuerzos']], index=0)
    with col2:
        almuerzo_2_dias = st.selectbox("Almuerzo Corto (Para 2 días):", [r['nombre'] for r in RECETARIO['Almuerzos']], index=1)

    st.markdown("---")
    st.markdown("### 2. Elige Desayunos y Cenas (Día a día)")
    
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    # Creamos diccionarios para guardar las elecciones
    elecciones_desayuno = {}
    elecciones_cena = {}

    c1, c2 = st.columns(2)
    
    for i, dia in enumerate(dias_semana):
        with c1:
            elecciones_desayuno[dia] = st.selectbox(f"Desayuno {dia}", [r['nombre'] for r in RECETARIO['Desayunos']], key=f"des_{i}")
        with c2:
            elecciones_cena[dia] = st.selectbox(f"Cena {dia}", [r['nombre'] for r in RECETARIO['Cenas']], key=f"cen_{i}")

# ==========================================
# 2. PESTAÑA: COCINA Y COMPRAS
# ==========================================
with tab_cocina:
    st.info("Aquí ves cuánto cocinar en TOTAL (para la olla) y cuánto servir en CADA PLATO.")

    # Función auxiliar para mostrar bloques de cocina
    def mostrar_bloque_cocina(titulo, receta_nombre, dias_duracion):
        # Buscamos la receta en todas las listas
        todas_las_recetas = RECETARIO['Almuerzos'] + RECETARIO['Desayunos'] + RECETARIO['Cenas']
        receta = next(r for r in todas_las_recetas if r['nombre'] == receta_nombre)
        
        with st.expander(f"🔥 {titulo}: {receta_nombre} ({dias_duracion} días)", expanded=True):
            st.markdown(f"**Ingredientes Totales a Cocinar** (Suma de Edimar + Carlos por {dias_duracion} días):")
            
            for ing in receta['ingredientes']:
                # Cálculos
                qty_e = ing['cantidad'] * factor_e
                qty_c = ing['cantidad'] * factor_c
                total_batch = (qty_e + qty_c) * dias_duracion
                
                # Mostrar
                st.write(f"- 🥘 **Olla Total:** {total_batch:.0f} {ing['unidad']} de {ing['item']}")
                st.caption(f"   ↳ 🍽️ Al emplatar: Edimar **{qty_e:.0f}{ing['unidad']}** | Carlos **{qty_c:.0f}{ing['unidad']}**")

    # MOSTRAR ALMUERZOS
    st.subheader("🍛 Preparación de Almuerzos")
    mostrar_bloque_cocina("Almuerzo Largo", almuerzo_3_dias, 3)
    mostrar_bloque_cocina("Almuerzo Corto", almuerzo_2_dias, 2)

    st.markdown("---")
    
    # LISTA DE COMPRAS
    st.subheader("🛒 Lista de Compras Total")
    if st.button("Generar Lista de Supermercado"):
        lista_final = {}

        def sumar_al_carrito(nombre, dias):
            todas_las_recetas = RECETARIO['Almuerzos'] + RECETARIO['Desayunos'] + RECETARIO['Cenas']
            receta = next(r for r in todas_las_recetas if r['nombre'] == nombre)
            
            for ing in receta['ingredientes']:
                qty_e = ing['cantidad'] * factor_e
                qty_c = ing['cantidad'] * factor_c
                total = (qty_e + qty_c) * dias
                
                if ing['item'] in lista_final:
                    lista_final[ing['item']] += total
                else:
                    lista_final[ing['item']] = total

        # Sumamos todo
        sumar_al_carrito(almuerzo_3_dias, 3)
        sumar_al_carrito(almuerzo_2_dias, 2)
        for dia in dias_semana:
            sumar_al_carrito(elecciones_desayuno[dia], 1)
            sumar_al_carrito(elecciones_cena[dia], 1)

        # Mostrar Tabla
        df = pd.DataFrame(list(lista_final.items()), columns=['Ingrediente', 'Cantidad Total'])
        # Formatear números para que no salgan decimales largos
        df['Cantidad Total'] = df['Cantidad Total'].apply(lambda x: f"{x:.1f}")
        st.dataframe(df, use_container_width=True)

# ==========================================
# 3. PESTAÑA: RECETARIO (CON CANTIDADES)
# ==========================================
with tab_recetario:
    st.header("📖 Tu Libro de Cocina")
    
    filtro = st.selectbox("Ver categoría:", ["Desayunos", "Almuerzos", "Cenas"])
    
    for receta in RECETARIO[filtro]:
        with st.expander(f"📌 {receta['nombre']}"):
            st.markdown(f"_{receta['descripcion']}_")
            
            st.markdown("### 🧬 Ingredientes (Tus Porciones)")
            st.info("Cantidades ajustadas a sus pesos actuales:")
            
            for ing in receta['ingredientes']:
                cant_e = round(ing['cantidad'] * factor_e)
                cant_c = round(ing['cantidad'] * factor_c)
                st.write(f"- **{ing['item']}**: 👩 Edimar `{cant_e} {ing['unidad']}` | 👨 Carlos `{cant_c} {ing['unidad']}`")
            
            st.markdown("### 👨‍🍳 Instrucciones")
            st.write(receta.get('instrucciones', 'Instrucciones pendientes.'))
