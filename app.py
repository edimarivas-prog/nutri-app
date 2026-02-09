import streamlit as st
import pandas as pd
from recetas import RECETARIO

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="NutriPlan Pro", page_icon="💪", layout="wide")

# Estilos
st.markdown("""
    <style>
    .stSelectbox label { font-size: 0.9rem; font-weight: bold; color: #4CAF50; }
    .block-container { padding-top: 2rem; }
    div[data-testid="column"] { background-color: #f9f9f9; padding: 10px; border-radius: 10px; border: 1px solid #eee;}
    </style>
""", unsafe_allow_html=True)

# --- MEMORIA (SESSION STATE) ---
if 'menu_semanal' not in st.session_state:
    st.session_state.menu_semanal = {
        "Desayuno": [RECETARIO['Desayunos'][0]['nombre']] * 7,
        "Cena": [RECETARIO['Cenas'][0]['nombre']] * 7
    }

# --- BARRA LATERAL ---
with st.sidebar:
    st.header("⚙️ Configuración")
    p_edimar = st.number_input("Peso Edimar (kg)", 60.0, 150.0, 102.0, 0.5)
    p_carlos = st.number_input("Peso Carlos (kg)", 60.0, 150.0, 81.0, 0.5)
    
    st.markdown("---")
    st.info("💡 **Tip:** Usa el botón de 'Relleno Rápido' para ganar tiempo.")

f_e = p_edimar / 102.0
f_c = p_carlos / 81.0

st.title("💪 NutriPlan: Alto Rendimiento")

# --- PESTAÑAS ---
tabs = st.tabs(["🗓️ Planificador", "📊 Calorías", "🛒 Compras", "👨‍🍳 Cocina"])

# ==================================================
# PESTAÑA 1: PLANIFICADOR
# ==================================================
with tabs[0]:
    st.subheader("🍛 Almuerzos (Ollas Semanales)")
    ca1, ca2 = st.columns(2)
    with ca1:
        alm_1 = st.selectbox("Olla 1 (Lun-Mié)", [r['nombre'] for r in RECETARIO['Almuerzos']], index=0)
    with ca2:
        alm_2 = st.selectbox("Olla 2 (Jue-Vie)", [r['nombre'] for r in RECETARIO['Almuerzos']], index=1)
    
    st.markdown("---")

    st.subheader("☀️ Desayunos y 🌙 Cenas")
    
    # HERRAMIENTA RÁPIDA
    with st.container():
        st.markdown("#### ⚡ Relleno Rápido")
        c_tool1, c_tool2, c_tool3 = st.columns([2, 2, 1])
        
        with c_tool1:
            base_des = st.selectbox("Desayuno Base:", [r['nombre'] for r in RECETARIO['Desayunos']])
        with c_tool2:
            base_cen = st.selectbox("Cena Base:", [r['nombre'] for r in RECETARIO['Cenas']])
        with c_tool3:
            st.write("") 
            st.write("") 
            if st.button("🚀 Aplicar a Todo"):
                st.session_state.menu_semanal["Desayuno"] = [base_des] * 7
                st.session_state.menu_semanal["Cena"] = [base_cen] * 7
                st.rerun()

    st.markdown("#### 📅 Ajuste Día por Día")
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    cols = st.columns(7)
    
    for i, dia in enumerate(dias):
        with cols[i]:
            st.markdown(f"**{dia}**")
            
            # Recuperar índices con seguridad
            try:
                idx_d = [r['nombre'] for r in RECETARIO['Desayunos']].index(st.session_state.menu_semanal["Desayuno"][i])
            except: idx_d = 0
                
            try:
                idx_c = [r['nombre'] for r in RECETARIO['Cenas']].index(st.session_state.menu_semanal["Cena"][i])
            except: idx_c = 0

            # Selectores
            new_d = st.selectbox("Des", [r['nombre'] for r in RECETARIO['Desayunos']], index=idx_d, key=f"d_{i}", label_visibility="collapsed")
            new_c = st.selectbox("Cen", [r['nombre'] for r in RECETARIO['Cenas']], index=idx_c, key=f"c_{i}", label_visibility="collapsed")
            
            # Actualizar memoria
            if new_d != st.session_state.menu_semanal["Desayuno"][i]:
                st.session_state.menu_semanal["Desayuno"][i] = new_d
                st.rerun()
            if new_c != st.session_state.menu_semanal["Cena"][i]:
                st.session_state.menu_semanal["Cena"][i] = new_c
                st.rerun()

# ==================================================
# PESTAÑA 2: AUDITORÍA
# ==================================================
with tabs[1]:
    st.header("📊 Semáforo Nutricional")
    
    def get_macros(nombre):
        # Buscamos en TODAS las listas, incluyendo Meriendas si fuera necesario
        pool = RECETARIO['Almuerzos'] + RECETARIO['Desayunos'] + RECETARIO['Cenas'] + RECETARIO.get('Meriendas', [])
        r = next((x for x in pool if x['nombre'] == nombre), None)
        return r['macros'] if r else {"cal":0, "prot":0}

    col_e, col_c = st.columns(2)
    
    # EDIMAR
    with col_e:
        st.subheader("👩 Edimar (Meta ~2200)")
        for i, dia in enumerate(dias):
            alm_actual = alm_1 if i < 3 else alm_2
            des = st.session_state.menu_semanal["Desayuno"][i]
            cen = st.session_state.menu_semanal["Cena"][i]
            
            # Sumar macros
            total = (get_macros(des)['cal'] + get_macros(alm_actual)['cal'] + get_macros(cen)['cal']) * f_e
            
            c1, c2 = st.columns([1, 2])
            c1.write(f"**{dia[:3]}**")
            if total < 1800: c2.error(f"{total:.0f} kcal (Bajo)")
            elif total > 2600: c2.warning(f"{total:.0f} kcal (Alto)")
            else: c2.success(f"{total:.0f} kcal ✅")

    # CARLOS
    with col_c:
        st.subheader("👨 Carlos (Meta ~2400)")
        for i, dia in enumerate(dias):
            alm_actual = alm_1 if i < 3 else alm_2
            des = st.session_state.menu_semanal["Desayuno"][i]
            cen = st.session_state.menu_semanal["Cena"][i]
            
            total = (get_macros(des)['cal'] + get_macros(alm_actual)['cal'] + get_macros(cen)['cal']) * f_c
            
            c1, c2 = st.columns([1, 2])
            c1.write(f"**{dia[:3]}**")
            if total < 2000: c2.error(f"{total:.0f} kcal (Bajo)")
            else: c2.success(f"{total:.0f} kcal ✅")

# ==================================================
# PESTAÑA 3: COMPRAS
# ==================================================
with tabs[2]:
    if st.button("🛒 Generar Lista", type="primary"):
        lista = {}
        def add(nombre, dias):
            pool = RECETARIO['Almuerzos'] + RECETARIO['Desayunos'] + RECETARIO['Cenas'] + RECETARIO.get('Meriendas', [])
            r = next((x for x in pool if x['nombre'] == nombre), None)
            if r:
                for ing in r['ingredientes']:
                    p = ing.get('pasillo', 'Otros')
                    k = ing['item']
                    q = (ing['cantidad'] * f_e + ing['cantidad'] * f_c) * dias
                    if p not in lista: lista[p] = {}
                    if k not in lista[p]: lista[p][k] = 0
                    lista[p][k] += q
        
        add(alm_1, 3)
        add(alm_2, 4)
        for d in st.session_state.menu_semanal["Desayuno"]: add(d, 1)
        for c in st.session_state.menu_semanal["Cena"]: add(c, 1)
        
        c1, c2 = st.columns(2)
        items = sorted(list(lista.items()))
        mitad = (len(items)//2) + 1
        
        with c1:
            for p, prods in items[:mitad]:
                with st.expander(p, expanded=True):
                    for k, v in prods.items(): st.checkbox(f"{k}: {v:.0f}")
        with c2:
            for p, prods in items[mitad:]:
                with st.expander(p, expanded=True):
                    for k, v in prods.items(): st.checkbox(f"{k}: {v:.0f}")

# ==================================================
# PESTAÑA 4: COCINA (CORREGIDA)
# ==================================================
with tabs[3]:
    st.header("👨‍🍳 Libro de Recetas")
    
    col_sel, col_view = st.columns([1, 2])
    
    with col_sel:
        # Agregamos "Meriendas" al selector
        cat = st.selectbox("Categoría", ["Almuerzos", "Desayunos", "Cenas", "Meriendas"])
        
        # Filtramos para que no falle si la categoría está vacía
        opciones = [r['nombre'] for r in RECETARIO.get(cat, [])]
        plato = st.radio("Elige el plato:", opciones)
    
    with col_view:
        # Creamos una "piscina" con todas las recetas para buscar
        pool = RECETARIO['Almuerzos'] + RECETARIO['Desayunos'] + RECETARIO['Cenas'] + RECETARIO.get('Meriendas', [])
        
        receta = next((x for x in pool if x['nombre'] == plato), None)
        
        if receta:
            st.markdown(f"## 📌 {receta['nombre']}")
            
            # --- AQUÍ ESTABA EL ERROR DE INDENTACIÓN (YA CORREGIDO) ---
            # Usamos .get() para evitar error si no hay descripción
            st.markdown(f"_{receta.get('descripcion', 'Sin descripción disponible')}_")
            
            # Macros
            m = receta.get('macros', {'cal':0, 'prot':0, 'carb':0, 'fat':0})
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Calorías", f"{m['cal']}")
            c2.metric("Proteína", f"{m['prot']}g")
            c3.metric("Carbos", f"{m['carb']}g")
            c4.metric("Grasas", f"{m['fat']}g")
            
            st.divider()
            
            # Ingredientes
            st.markdown("#### ⚖️ Cantidades")
            df_ing = []
            for i in receta['ingredientes']:
                df_ing.append({
                    "Ingrediente": i['item'],
                    "Edimar": f"{i['cantidad']*f_e:.0f} {i['unidad']}",
                    "Carlos": f"{i['cantidad']*f_c:.0f} {i['unidad']}"
                })
            st.table(pd.DataFrame(df_ing))
            
            # Instrucciones
            st.info(f"📝 **Instrucciones:**\n\n{receta.get('instrucciones', 'Pasos no disponibles.')}")
