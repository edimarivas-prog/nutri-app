import streamlit as st
import pandas as pd
from recetas import RECETARIO

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="NutriPlan 2.0", page_icon="🥗", layout="wide")

# --- ESTILOS CSS (Para que se vea menos 'tsco') ---
st.markdown("""
    <style>
    .big-font { font-size:20px !important; font-weight: bold; }
    .stSelectbox label { font-size: 18px; font-weight: bold; }
    div[data-testid="stExpander"] div[role="button"] p { font-size: 1.1rem; }
    </style>
    """, unsafe_allow_html=True)

# --- DATOS USUARIO ---
st.sidebar.title("👤 Perfil")
peso_edimar = st.sidebar.number_input("Peso Edimar (kg)", 60.0, 150.0, 102.0, 0.5)
peso_carlos = st.sidebar.number_input("Peso Carlos (kg)", 60.0, 150.0, 81.0, 0.5)

factor_e = peso_edimar / 102.0
factor_c = peso_carlos / 81.0

# --- TÍTULO ---
st.title("🥗 Planificador Inteligente")
st.markdown("---")

# ==========================================
# 1. SECCIÓN: PLANIFICACIÓN (Lógica Mejorada)
# ==========================================
c1, c2 = st.columns([1, 1])

with c1:
    st.markdown("### 🥘 Almuerzos (Batch Cooking)")
    st.info("Selecciona tus 2 preparaciones de la semana.")
    
    # Lógica Batch Cooking
    almuerzo_largo = st.selectbox("🥣 Olla Grande (Lunes, Martes, Miércoles)", [r['nombre'] for r in RECETARIO['Almuerzos']], index=0)
    almuerzo_corto = st.selectbox("🥣 Olla Pequeña (Jueves, Viernes)", [r['nombre'] for r in RECETARIO['Almuerzos']], index=1)

with c2:
    st.markdown("### 🍳 Desayuno y 🌙 Cena")
    
    # Lógica de Repetición (FIX DE USABILIDAD)
    col_des, col_cen = st.columns(2)
    
    with col_des:
        desayuno_base = st.selectbox("Desayuno Base", [r['nombre'] for r in RECETARIO['Desayunos']])
        repetir_des = st.checkbox("¿Desayunar esto toda la semana?", value=True)
    
    with col_cen:
        cena_base = st.selectbox("Cena Base", [r['nombre'] for r in RECETARIO['Cenas']])
        repetir_cen = st.checkbox("¿Cenar esto toda la semana?", value=True)

# --- GENERADOR DE MENÚ DIARIO (Backend) ---
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
menu_semanal = {"Día": [], "Desayuno": [], "Almuerzo": [], "Cena": []}

for i, dia in enumerate(dias):
    menu_semanal["Día"].append(dia)
    
    # Lógica Desayuno
    if repetir_des:
        platillo = desayuno_base
    else:
        platillo = st.selectbox(f"Desayuno {dia}", [r['nombre'] for r in RECETARIO['Desayunos']], key=f"d_{i}")
    menu_semanal["Desayuno"].append(platillo)
    
    # Lógica Almuerzo (Batch)
    if dia in ["Lunes", "Martes", "Miércoles"]:
        menu_semanal["Almuerzo"].append(almuerzo_largo)
    elif dia in ["Jueves", "Viernes"]:
        menu_semanal["Almuerzo"].append(almuerzo_corto)
    else:
        menu_semanal["Almuerzo"].append("Libre / Sobras") # Sábado y Domingo

    # Lógica Cena
    if repetir_cen:
        platillo_c = cena_base
    else:
        platillo_c = st.selectbox(f"Cena {dia}", [r['nombre'] for r in RECETARIO['Cenas']], key=f"c_{i}")
    menu_semanal["Cena"].append(platillo_c)

# Visualización del Calendario
with st.expander("📅 Ver Tu Calendario Semanal Generado", expanded=True):
    st.dataframe(pd.DataFrame(menu_semanal), use_container_width=True, hide_index=True)

st.markdown("---")

# ==========================================
# 2. SECCIÓN: COCINA (Cantidades Totales)
# ==========================================
st.markdown("## 🔪 A Cocinar")
tab_cocina, tab_compras = st.tabs(["🔥 Guía de Preparación", "🛒 Lista de Compras"])

with tab_cocina:
    col_a, col_b = st.columns(2)
    
    # Función para mostrar tarjeta de receta
    def tarjeta_receta(titulo, nombre, dias_count):
        # Buscar receta
        pool = RECETARIO['Almuerzos'] + RECETARIO['Desayunos'] + RECETARIO['Cenas']
        receta = next((r for r in pool if r['nombre'] == nombre), None)
        
        if receta:
            st.markdown(f"### {titulo}")
            st.markdown(f"**Plato:** {nombre}")
            st.warning(f"⚠️ Cocinar para **{dias_count} días**")
            
            # Tabla de ingredientes
            data_ing = []
            for ing in receta['ingredientes']:
                total_batch = (ing['cantidad'] * factor_e + ing['cantidad'] * factor_c) * dias_count
                porcion_e = ing['cantidad'] * factor_e
                porcion_c = ing['cantidad'] * factor_c
                
                data_ing.append({
                    "Ingrediente": ing['item'],
                    "Total Olla": f"{total_batch:.0f} {ing['unidad']}",
                    "Plato Edimar": f"{porcion_e:.0f}",
                    "Plato Carlos": f"{porcion_c:.0f}"
                })
            
            st.table(pd.DataFrame(data_ing))
            st.markdown(f"**📝 Pasos:** {receta.get('instrucciones', '...')}")
            st.markdown("---")

    with col_a:
        tarjeta_receta("🥣 OLLA 1 (Lun-Mié)", almuerzo_largo, 3)
    
    with col_b:
        tarjeta_receta("🥣 OLLA 2 (Jue-Vie)", almuerzo_corto, 2)
    
    st.info("💡 Nota: Los desayunos y cenas se cocinan al día, las porciones son individuales.")

# ==========================================
# 3. SECCIÓN: COMPRAS (Lógica Agrupada)
# ==========================================
with tab_compras:
    if st.button("Generar Lista Definitiva", type="primary"):
        lista_final = {}

        def sumar(nombre, dias):
             # Buscar receta en todas las listas
            pool = RECETARIO['Almuerzos'] + RECETARIO['Desayunos'] + RECETARIO['Cenas']
            r = next((x for x in pool if x['nombre'] == nombre), None)
            if r:
                for ing in r['ingredientes']:
                    total = (ing['cantidad']*factor_e + ing['cantidad']*factor_c) * dias
                    if ing['item'] in lista_final:
                        lista_final[ing['item']] += total
                    else:
                        lista_final[ing['item']] = total

        # Procesar Almuerzos
        sumar(almuerzo_largo, 3)
        sumar(almuerzo_corto, 2)
        
        # Procesar Desayunos/Cenas (recorriendo el menú generado)
        for d in menu_semanal["Desayuno"]:
            sumar(d, 1)
        for c in menu_semanal["Cena"]:
            sumar(c, 1)

        # Mostrar bonito
        st.success("✅ Lista generada con éxito")
        
        df_compras = pd.DataFrame(list(lista_final.items()), columns=["Producto", "Cantidad Total"])
        df_compras['Cantidad Total'] = df_compras['Cantidad Total'].apply(lambda x: f"{x:.1f}")
        
        st.dataframe(df_compras, use_container_width=True, height=500)
