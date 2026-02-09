import streamlit as st
import pandas as pd
import altair as alt # Para gráficos bonitos
from recetas import RECETARIO

# --- CONFIGURACIÓN "APP MÓVIL" ---
st.set_page_config(page_title="NutriApp Pro", page_icon="🥗", layout="centered")

# Estilos CSS para que parezca una App real y no una web
st.markdown("""
    <style>
    .stSelectbox label { font-weight: bold; font-size: 1.1rem; color: #4CAF50; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { border-radius: 4px 4px 0 0; background-color: #f0f2f6; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { background-color: #4CAF50; color: white; }
    h1, h2, h3 { color: #333; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR: DATOS Y PROGRESO ---
with st.sidebar:
    st.header("📉 Tu Progreso")
    
    # Simulación de datos históricos (luego podríamos guardarlos real)
    data_progreso = pd.DataFrame({
        'Semana': [1, 2, 3, 4],
        'Peso Edimar': [105, 104, 103, 102],
        'Peso Carlos': [83, 82.5, 81.8, 81]
    })
    
    # Inputs Actuales
    st.subheader("⚖️ Pesaje Semanal")
    p_edimar = st.number_input("Edimar (kg)", 60.0, 150.0, 102.0, 0.5)
    p_carlos = st.number_input("Carlos (kg)", 60.0, 150.0, 81.0, 0.5)
    
    # Gráfico Miniatura
    chart = alt.Chart(data_progreso).mark_line(point=True).encode(
        x='Semana',
        y=alt.Y('Peso Edimar', scale=alt.Scale(zero=False)),
        tooltip=['Semana', 'Peso Edimar']
    ).properties(height=150, title="Evolución Edimar")
    st.altair_chart(chart, use_container_width=True)

# Factores de Ajuste
f_e = p_edimar / 102.0
f_c = p_carlos / 81.0

# --- HEADER CON MÉTRICAS ---
st.title("🥗 NutriApp Fusión")
col_m1, col_m2 = st.columns(2)
col_m1.metric("Objetivo Edimar", f"{int(2050 * f_e)} kcal", "-500 kcal")
col_m2.metric("Objetivo Carlos", f"{int(2100 * f_c)} kcal", "-500 kcal")

# --- PESTAÑAS PRINCIPALES ---
tabs = st.tabs(["🗓️ Planificar", "🛒 Compras (Smart)", "👨‍🍳 Cocinar"])

# ==================================================
# PESTAÑA 1: PLANIFICADOR VISUAL
# ==================================================
with tabs[0]:
    st.markdown("### 🍛 Almuerzos de la Semana")
    st.info("Selecciona los 2 platos fuertes para Batch Cooking")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**🥣 Olla 1 (Lun-Mié)**")
        almuerzo_1 = st.selectbox("Seleccionar Menú A", [r['nombre'] for r in RECETARIO['Almuerzos']], index=0, label_visibility="collapsed")
        # Aquí podrías poner st.image(url_imagen) si la tuvieras en recetas.py
    
    with c2:
        st.markdown("**🥣 Olla 2 (Jue-Vie)**")
        almuerzo_2 = st.selectbox("Seleccionar Menú B", [r['nombre'] for r in RECETARIO['Almuerzos']], index=1, label_visibility="collapsed")

    st.markdown("---")
    st.markdown("### ☀️ Desayunos y 🌙 Cenas")
    
    check_repeat = st.checkbox("🔄 Comer lo mismo toda la semana (Modo Ahorro Tiempo)", value=True)
    
    if check_repeat:
        col_d, col_c = st.columns(2)
        with col_d:
            des_base = st.selectbox("Desayuno Único", [r['nombre'] for r in RECETARIO['Desayunos']])
        with col_c:
            cen_base = st.selectbox("Cena Única", [r['nombre'] for r in RECETARIO['Cenas']])
        
        # Generamos el menú interno
        menu = {"Desayuno": [des_base]*7, "Cena": [cen_base]*7}
    else:
        # Aquí iría el selector día por día si desactivan el checkbox
        st.warning("Modo detallado desactivado por simplicidad en esta demo.")
        menu = {"Desayuno": [RECETARIO['Desayunos'][0]['nombre']]*7, "Cena": [RECETARIO['Cenas'][0]['nombre']]*7}

# ==================================================
# PESTAÑA 2: COMPRAS INTELIGENTES (POR PASILLO)
# ==================================================
with tabs[1]:
    st.header("🛒 Lista de Supermercado")
    
    if st.button("Generar Lista Organizada", type="primary"):
        lista_smart = {} # Diccionario: {'Verdulería': {'Cebolla': 500}, ...}

        def agregar_smart(nombre_receta, dias):
             # Buscar receta
            pool = RECETARIO['Almuerzos'] + RECETARIO['Desayunos'] + RECETARIO['Cenas']
            r = next((x for x in pool if x['nombre'] == nombre_receta), None)
            
            if r:
                for ing in r['ingredientes']:
                    pasillo = ing.get('pasillo', 'Otros') # Si no tiene pasillo, va a Otros
                    item = ing['item']
                    total = (ing['cantidad'] * f_e + ing['cantidad'] * f_c) * dias
                    
                    if pasillo not in lista_smart:
                        lista_smart[pasillo] = {}
                    
                    if item in lista_smart[pasillo]:
                        lista_smart[pasillo][item] += total
                    else:
                        lista_smart[pasillo][item] = total

        # Procesar
        agregar_smart(almuerzo_1, 3)
        agregar_smart(almuerzo_2, 2)
        agregar_smart(des_base, 7) if check_repeat else None
        agregar_smart(cen_base, 7) if check_repeat else None

        # MOSTRAR POR PASILLOS (VISUALMENTE HERMOSO)
        col_a, col_b = st.columns(2)
        
        items_vista = list(lista_smart.items())
        mitad = len(items_vista) // 2
        
        # Columna Izquierda
        with col_a:
            for pasillo, items in items_vista[:mitad]:
                with st.expander(f"{pasillo}", expanded=True):
                    for ingrediente, cantidad in items.items():
                        st.checkbox(f"**{ingrediente}**: {cantidad:.0f} g/ml")

        # Columna Derecha
        with col_b:
            for pasillo, items in items_vista[mitad:]:
                with st.expander(f"{pasillo}", expanded=True):
                    for ingrediente, cantidad in items.items():
                        st.checkbox(f"**{ingrediente}**: {cantidad:.0f} g/ml")

# ==================================================
# PESTAÑA 3: COCINA (PASO A PASO)
# ==================================================
with tabs[2]:
    st.header("👨‍🍳 Modo Cocina")
    
    opcion_cocinar = st.selectbox("¿Qué vas a cocinar hoy?", ["Olla 1 (Lun-Mié)", "Olla 2 (Jue-Vie)", "Desayuno del Día", "Cena del Día"])
    
    # Determinar qué receta mostrar
    receta_mostrar = None
    dias_factor = 1
    
    if opcion_cocinar == "Olla 1 (Lun-Mié)":
        receta_nombre = almuerzo_1
        dias_factor = 3
    elif opcion_cocinar == "Olla 2 (Jue-Vie)":
        receta_nombre = almuerzo_2
        dias_factor = 2
    elif opcion_cocinar == "Desayuno del Día":
        receta_nombre = des_base
        dias_factor = 1
    else:
        receta_nombre = cen_base
        dias_factor = 1

    # Mostrar detalles
    pool = RECETARIO['Almuerzos'] + RECETARIO['Desayunos'] + RECETARIO['Cenas']
    receta = next((x for x in pool if x['nombre'] == receta_nombre), None)

    if receta:
        st.markdown(f"## 📌 {receta['nombre']}")
        st.markdown(f"_{receta['descripcion']}_")
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Olla", f"x {dias_factor} días")
        c2.metric("Tu Plato", "Edimar")
        c3.metric("Su Plato", "Carlos")
        
        st.table(pd.DataFrame([
            {
                "Ingrediente": i['item'], 
                "Total Olla": f"{(i['cantidad']*(f_e+f_c)*dias_factor):.0f} {i['unidad']}",
                "Edimar": f"{(i['cantidad']*f_e):.0f}",
                "Carlos": f"{(i['cantidad']*f_c):.0f}"
            } for i in receta['ingredientes']
        ]))
        
        st.markdown("### 📝 Instrucciones")
        st.info(receta['instrucciones'])
