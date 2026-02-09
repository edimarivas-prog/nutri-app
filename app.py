import streamlit as st
import pandas as pd
from recetas import RECETARIO

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="NutriApp Ven-Per", page_icon="🥑", layout="wide")

# --- BARRA LATERAL (DATOS) ---
st.sidebar.header("⚙️ Tus Datos")

# CORRECCIÓN: Ahora definimos min_value (mínimo) y value (valor actual) por separado
peso_edimar = st.sidebar.number_input(
    "Peso Edimar (kg)", 
    min_value=60.0,   # Permite bajar hasta 60kg
    max_value=150.0, 
    value=102.0,      # Este es tu peso inicial
    step=0.5
)

peso_carlos = st.sidebar.number_input(
    "Peso Carlos (kg)", 
    min_value=60.0,   # Permite bajar hasta 60kg
    max_value=150.0, 
    value=81.0,       # Este es su peso inicial
    step=0.5
)

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

    # Usamos columnas para que no sea una lista eterna hacia abajo
    c1, c2 = st.columns(2)
    
    for i, dia in enumerate(dias_semana):
        # Desayunos en columna 1
        with c1:
            elecciones_desayuno[dia] = st.selectbox(f"Desayuno {dia}", [r['nombre'] for r in RECETARIO['Desayunos']], key=f"des_{i}")
        # Cenas en columna 2
        with c2:
            elecciones_cena[dia] = st.selectbox(f"Cena {dia}", [r['nombre'] for r in RECETARIO['Cenas']], key=f"cen_{i}")

# ==========================================
# 2. PESTAÑA: COCINA Y COMPRAS
# ==========================================
with tab_cocina:
    st.info("Aquí ves cuánto cocinar en TOTAL (para la olla) y cuánto servir en CADA PLATO.")

    # --- FUNCIÓN MAESTRA DE CÁLCULO ---
    def mostrar_bloque_cocina(titulo, receta_nombre, dias_duracion):
        receta = next(r for r in RECETARIO['Almuerzos'] + RECETARIO['Desayunos'] + RECETARIO['Cenas'] if r['nombre'] == receta_nombre)
        
        with st.expander(f"🔥 {titulo}: {receta_nombre} ({dias_duracion} días)", expanded=True):
            st.markdown(f"**Ingredientes Totales a Cocinar** (Suma de Edimar + Carlos por {dias_duracion} días):")
            
            for ing in receta['ingredientes']:
                # 1. Calculamos la porción individual ajustada al peso
                qty_e = ing['cantidad'] * factor_e
                qty_c = ing['cantidad'] * factor_c
                
                # 2. Sumamos lo que comen ambos en un día
                total_diario = qty_e + qty_c
                
                # 3. Multiplicamos por los días que van a comer eso
                total_batch = total_diario * dias_duracion
                
                # Mostramos la fila
                st.write(f"- 🥘 **Olla Total:** {total_batch:.0f} {ing['unidad']} de {ing['item']}")
                st.caption(f"   ↳ 🍽️ Al emplatar: Edimar **{qty_e:.0f}{ing['unidad']}** | Carlos **{qty_c:.0f}{ing['unidad']}**")

    # MOSTRAR ALMUERZOS
    st.subheader("🍛 Preparación de Almuerzos")
    mostrar_bloque_cocina("Almuerzo Largo", almuerzo_3_dias, 3)
    mostrar_bloque_cocina("Almuerzo Corto", almuerzo_2_dias, 2)

    st.markdown("---")
    
    # LISTA DE COMPRAS (Agregada al final de esta pestaña)
    st.subheader("🛒 Lista de Compras Total")
    if st.button("Generar Lista de Supermercado"):
        lista_final = {}

        def sumar_al_carrito(nombre, dias):
            receta = next(r for r in RECETARIO['Almuerzos'] + RECETARIO['Desayunos'] + RECETARIO['Cenas'] if r['nombre'] == nombre)
            for ing in receta['ingredientes']:
                qty_e = ing['cantidad'] * factor_e
                qty_c = ing['cantidad'] * factor_c
                total = (qty_e + qty_c) * dias
                
                if ing['item'] in lista_final:
                    lista_final[ing['item']] += total
                else:
                    lista_final[ing['item']] = total

        # Sumar Almuerzos
        sumar_al_carrito(almuerzo_3_dias, 3)
        sumar_al_carrito(almuerzo_2_dias, 2)
        
        # Sumar Desayunos y Cenas (Uno por uno según selección)
        for dia in dias_semana:
            sumar_al_carrito(elecciones_desayuno[dia], 1)
            sumar_al_carrito(elecciones_cena[dia], 1)

        # Mostrar Tabla
        df = pd.DataFrame(list(lista_final.items()), columns=['Ingrediente', 'Cantidad Total'])
        st.dataframe(df, use_container_width=True)

# ==========================================
# 3. PESTAÑA: RECETARIO (LIBRO DE COCINA)
# ==========================================
with tab_recetario:
    st.header("📖 Tu Libro de Cocina")
    
    filtro = st.selectbox("Ver categoría:", ["Desayunos", "Almuerzos", "Cenas"])
    
    for receta in RECETARIO[filtro]:
        with st.expander(f"📌 {receta['nombre']}"):
            st.write(f"_{receta['descripcion']}_")
            st.markdown("**Ingredientes Base:**")
            for ing in receta['ingredientes']:
                st.write(f"- {ing['item']}")
            
            st.markdown("**👨‍🍳 Paso a Paso:**")
            st.write(receta.get('instrucciones', 'No hay instrucciones detalladas aún.'))
