import streamlit as st
import pandas as pd
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

# --- INICIALIZAR ESTADO (Para que la lista no desaparezca) ---
if 'lista_compras' not in st.session_state:
    st.session_state.lista_compras = {}
if 'mostrar_lista' not in st.session_state:
    st.session_state.mostrar_lista = False

# --- SIDEBAR: DATOS ---
with st.sidebar:
    st.header("📉 Tu Progreso")
    st.subheader("⚖️ Pesaje Semanal")
    p_edimar = st.number_input("Edimar (kg)", 60.0, 150.0, 102.0, 0.5)
    p_carlos = st.number_input("Carlos (kg)", 60.0, 150.0, 81.0, 0.5)

# Factores de Ajuste
f_e = p_edimar / 102.0
f_c = p_carlos / 81.0

# --- HEADER ---
st.title("🥗 NutriApp Fusión 3.0")

# --- PESTAÑAS PRINCIPALES ---
tabs = st.tabs(["🗓️ Planificar", "🛒 Compras (Smart)", "👨‍🍳 Cocinar"])

# ==================================================
# PESTAÑA 1: PLANIFICADOR
# ==================================================
with tabs[0]:
    st.markdown("### 🍛 Almuerzos (Batch Cooking)")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**🥣 Olla 1 (Lun-Mié)**")
        almuerzo_1 = st.selectbox("Menú A", [r['nombre'] for r in RECETARIO['Almuerzos']], index=0, label_visibility="collapsed")
    with c2:
        st.markdown("**🥣 Olla 2 (Jue-Vie)**")
        almuerzo_2 = st.selectbox("Menú B", [r['nombre'] for r in RECETARIO['Almuerzos']], index=1, label_visibility="collapsed")

    st.markdown("---")
    st.markdown("### ☀️ Desayunos y 🌙 Cenas")
    
    check_repeat = st.checkbox("🔄 Comer lo mismo toda la semana", value=True)
    
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    menu_diario = {"Desayuno": [], "Cena": []}

    if check_repeat:
        col_d, col_c = st.columns(2)
        with col_d:
            des_base = st.selectbox("Desayuno Único", [r['nombre'] for r in RECETARIO['Desayunos']])
        with col_c:
            cen_base = st.selectbox("Cena Única", [r['nombre'] for r in RECETARIO['Cenas']])
        
        # Rellenamos la lista para los 7 días igual
        menu_diario["Desayuno"] = [des_base] * 7
        menu_diario["Cena"] = [cen_base] * 7
    
    else:
        st.info("Personaliza cada día:")
        for i, dia in enumerate(dias_semana):
            st.markdown(f"**{dia}**")
            c_d, c_c = st.columns(2)
            with c_d:
                d_sel = st.selectbox(f"Desayuno {dia}", [r['nombre'] for r in RECETARIO['Desayunos']], key=f"d_{i}", label_visibility="collapsed")
            with c_c:
                c_sel = st.selectbox(f"Cena {dia}", [r['nombre'] for r in RECETARIO['Cenas']], key=f"c_{i}", label_visibility="collapsed")
            
            menu_diario["Desayuno"].append(d_sel)
            menu_diario["Cena"].append(c_sel)

# ==================================================
# PESTAÑA 2: COMPRAS (ARREGLADA)
# ==================================================
with tabs[1]:
    st.header("🛒 Lista de Supermercado")
    
    if st.button("Generar Lista Organizada", type="primary"):
        st.session_state.mostrar_lista = True
        st.session_state.lista_compras = {} # Reiniciar lista

        def agregar_smart(nombre_receta, dias):
            pool = RECETARIO['Almuerzos'] + RECETARIO['Desayunos'] + RECETARIO['Cenas']
            r = next((x for x in pool if x['nombre'] == nombre_receta), None)
            
            if r:
                for ing in r['ingredientes']:
                    pasillo = ing.get('pasillo', 'Otros')
                    item = ing['item']
                    total = (ing['cantidad'] * f_e + ing['cantidad'] * f_c) * dias
                    
                    if pasillo not in st.session_state.lista_compras:
                        st.session_state.lista_compras[pasillo] = {}
                    
                    if item in st.session_state.lista_compras[pasillo]:
                        st.session_state.lista_compras[pasillo][item] += total
                    else:
                        st.session_state.lista_compras[pasillo][item] = total

        # 1. Sumar Almuerzos
        agregar_smart(almuerzo_1, 3)
        agregar_smart(almuerzo_2, 2)
        
        # 2. Sumar Desayunos y Cenas (recorriendo la lista generada arriba)
        for plato_d in menu_diario["Desayuno"]:
            agregar_smart(plato_d, 1)
        for plato_c in menu_diario["Cena"]:
            agregar_smart(plato_c, 1)

    # MOSTRAR LISTA (Si ya se generó)
    if st.session_state.mostrar_lista:
        col_a, col_b = st.columns(2)
        items_vista = list(st.session_state.lista_compras.items())
        
        # Dividir en dos columnas visuales
        mitad = (len(items_vista) // 2) + 1
        
        with col_a:
            for pasillo, items in items_vista[:mitad]:
                with st.container(border=True):
                    st.markdown(f"**{pasillo}**")
                    for ingrediente, cantidad in items.items():
                        st.checkbox(f"{ingrediente}: {cantidad:.0f} {list(RECETARIO['Desayunos'][0]['ingredientes'][0].keys())[2] if 'unidad' not in ingrediente else ''}", key=f"{pasillo}_{ingrediente}")

        with col_b:
            for pasillo, items in items_vista[mitad:]:
                 with st.container(border=True):
                    st.markdown(f"**{pasillo}**")
                    for ingrediente, cantidad in items.items():
                        st.checkbox(f"{ingrediente}: {cantidad:.0f}", key=f"{pasillo}_{ingrediente}")

# ==================================================
# PESTAÑA 3: COCINA
# ==================================================
with tabs[2]:
    st.header("👨‍🍳 Modo Cocina")
    opcion = st.selectbox("¿Qué cocinas hoy?", ["Olla 1 (Lun-Mié)", "Olla 2 (Jue-Vie)", "Desayuno Hoy", "Cena Hoy"])
    
    receta_nombre = None
    dias_factor = 1
    
    if opcion == "Olla 1 (Lun-Mié)":
        receta_nombre = almuerzo_1
        dias_factor = 3
    elif opcion == "Olla 2 (Jue-Vie)":
        receta_nombre = almuerzo_2
        dias_factor = 2
    elif opcion == "Desayuno Hoy":
        # Toma el primer desayuno de la lista (asumiendo que hoy es Lunes o genérico)
        receta_nombre = menu_diario["Desayuno"][0]
        dias_factor = 1
    else:
        receta_nombre = menu_diario["Cena"][0]
        dias_factor = 1

    pool = RECETARIO['Almuerzos'] + RECETARIO['Desayunos'] + RECETARIO['Cenas']
    receta = next((x for x in pool if x['nombre'] == receta_nombre), None)

    if receta:
        st.markdown(f"## 📌 {receta['nombre']}")
        
        # Macros
        if 'macros' in receta:
            m = receta['macros']
            c_m = st.columns(4)
            c_m[0].metric("Calorías", f"{m['cal']*f_e:.0f}")
            c_m[1].metric("Prot", f"{m['prot']*f_e:.1f}g")
            c_m[2].metric("Carb", f"{m['carb']*f_e:.1f}g")
            c_m[3].metric("Grasa", f"{m['fat']*f_e:.1f}g")

        st.table(pd.DataFrame([
            {
                "Ingrediente": i['item'], 
                "Total Olla": f"{(i['cantidad']*(f_e+f_c)*dias_factor):.0f} {i['unidad']}",
                "Edimar": f"{(i['cantidad']*f_e):.0f}",
                "Carlos": f"{(i['cantidad']*f_c):.0f}"
            } for i in receta['ingredientes']
        ]))
        st.info(receta['instrucciones'])
