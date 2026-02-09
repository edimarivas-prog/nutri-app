import streamlit as st
import pandas as pd
import altair as alt 
from recetas import RECETARIO

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="NutriPlan Pro", page_icon="🥗", layout="centered")

# Estilos CSS
st.markdown("""
    <style>
    .stSelectbox label { font-weight: bold; font-size: 1.1rem; color: #4CAF50; }
    h1, h2, h3 { color: #333; }
    div[data-testid="metric-container"] { background-color: #f0f2f6; border-radius: 8px; padding: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR: DATOS Y PROGRESO ---
with st.sidebar:
    st.header("📉 Tu Progreso")
    
    # Inputs Actuales
    st.subheader("⚖️ Pesaje Semanal")
    p_edimar = st.number_input("Edimar (kg)", 60.0, 150.0, 102.0, 0.5)
    p_carlos = st.number_input("Carlos (kg)", 60.0, 150.0, 81.0, 0.5)

# Factores de Ajuste
f_e = p_edimar / 102.0
f_c = p_carlos / 81.0

# --- HEADER ---
st.title("🥗 NutriApp Fusión 2.0")
st.caption("Planificador Inteligente con Macros y Lista de Compras")

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
    else:
        st.warning("Modo detallado desactivado por simplicidad en esta demo.")
        des_base = RECETARIO['Desayunos'][0]['nombre']
        cen_base = RECETARIO['Cenas'][0]['nombre']

# ==================================================
# PESTAÑA 2: COMPRAS INTELIGENTES
# ==================================================
with tabs[1]:
    st.header("🛒 Lista de Supermercado")
    
    if st.button("Generar Lista Organizada", type="primary"):
        lista_smart = {} 

        def agregar_smart(nombre_receta, dias):
            pool = RECETARIO['Almuerzos'] + RECETARIO['Desayunos'] + RECETARIO['Cenas']
            r = next((x for x in pool if x['nombre'] == nombre_receta), None)
            
            if r:
                for ing in r['ingredientes']:
                    pasillo = ing.get('pasillo', 'Otros')
                    item = ing['item']
                    total = (ing['cantidad'] * f_e + ing['cantidad'] * f_c) * dias
                    
                    if pasillo not in lista_smart:
                        lista_smart[pasillo] = {}
                    if item in lista_smart[pasillo]:
                        lista_smart[pasillo][item] += total
                    else:
                        lista_smart[pasillo][item] = total

        agregar_smart(almuerzo_1, 3)
        agregar_smart(almuerzo_2, 2)
        agregar_smart(des_base, 7) if check_repeat else None
        agregar_smart(cen_base, 7) if check_repeat else None

        col_a, col_b = st.columns(2)
        items_vista = list(lista_smart.items())
        mitad = len(items_vista) // 2
        
        with col_a:
            for pasillo, items in items_vista[:mitad]:
                with st.expander(f"{pasillo}", expanded=True):
                    for ingrediente, cantidad in items.items():
                        st.checkbox(f"**{ingrediente}**: {cantidad:.0f} g/ml")
        with col_b:
            for pasillo, items in items_vista[mitad:]:
                with st.expander(f"{pasillo}", expanded=True):
                    for ingrediente, cantidad in items.items():
                        st.checkbox(f"**{ingrediente}**: {cantidad:.0f} g/ml")

# ==================================================
# PESTAÑA 3: COCINA (CON MACROS)
# ==================================================
with tabs[2]:
    st.header("👨‍🍳 Modo Cocina")
    
    opcion_cocinar = st.selectbox("¿Qué vas a cocinar hoy?", ["Olla 1 (Lun-Mié)", "Olla 2 (Jue-Vie)", "Desayuno del Día", "Cena del Día"])
    
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

    pool = RECETARIO['Almuerzos'] + RECETARIO['Desayunos'] + RECETARIO['Cenas']
    receta = next((x for x in pool if x['nombre'] == receta_nombre), None)

    if receta:
        st.markdown(f"## 📌 {receta['nombre']}")
        st.markdown(f"_{receta['descripcion']}_")

        # --- SECCIÓN DE MACROS (NUEVO) ---
        st.markdown("### 📊 Información Nutricional (Por Plato)")
        col_user = st.radio("Ver macros para:", ["Edimar", "Carlos"], horizontal=True)
        
        # Seleccionamos el factor según el usuario
        f_user = f_e if col_user == "Edimar" else f_c
        
        # Calculamos macros escalados
        macros = receta.get('macros', {'cal':0, 'prot':0, 'carb':0, 'fat':0})
        
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Calorías", f"{macros['cal'] * f_user:.0f}", "Kcal")
        m2.metric("Proteína", f"{macros['prot'] * f_user:.1f}g", "💪")
        m3.metric("Carbos", f"{macros['carb'] * f_user:.1f}g", "🍞")
        m4.metric("Grasas", f"{macros['fat'] * f_user:.1f}g", "🥑")
        
        st.markdown("---")
        
        # TABLA DE INGREDIENTES
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
