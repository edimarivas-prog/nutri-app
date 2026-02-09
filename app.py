import streamlit as st
import pandas as pd
from recetas import RECETARIO

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="NutriPlan Pro", page_icon="💪", layout="wide")

# Estilos para que los selectores se vean compactos
st.markdown("""
    <style>
    .stSelectbox label { font-size: 0.9rem; font-weight: bold; color: #4CAF50; }
    .block-container { padding-top: 2rem; }
    div[data-testid="column"] { background-color: #f9f9f9; padding: 10px; border-radius: 10px; border: 1px solid #eee;}
    </style>
""", unsafe_allow_html=True)

# --- GESTIÓN DE ESTADO (MEMORIA DE LA APP) ---
# Esto permite que la app recuerde tu menú aunque hagas clic en otros botones
if 'menu_semanal' not in st.session_state:
    # Inicializamos todo con la primera receta de la lista
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
    st.info("💡 **Tip:** Usa el botón de 'Relleno Rápido' para poner lo mismo varios días y luego edita solo el día que quieras cambiar.")

f_e = p_edimar / 102.0
f_c = p_carlos / 81.0

st.title("💪 NutriPlan: Flexible")

# --- PESTAÑAS ---
tabs = st.tabs(["🗓️ Planificador", "📊 Calorías (Semáforo)", "🛒 Lista Compras", "👨‍🍳 Cocina"])

# ==================================================
# PESTAÑA 1: PLANIFICADOR HÍBRIDO
# ==================================================
with tabs[0]:
    # --- 1. ALMUERZOS (BATCH COOKING) ---
    st.subheader("🍛 Almuerzos")
    ca1, ca2 = st.columns(2)
    with ca1:
        alm_1 = st.selectbox("Almuerzo 1 (Lunes - Miércoles)", [r['nombre'] for r in RECETARIO['Almuerzos']], index=0)
    with ca2:
        alm_2 = st.selectbox("Almuerzo 2 (Jueves - Viernes)", [r['nombre'] for r in RECETARIO['Almuerzos']], index=1)
    
    st.markdown("---")

    # --- 2. DESAYUNOS Y CENAS (HERRAMIENTA DE RELLENO) ---
    st.subheader("☀️ Desayunos y 🌙 Cenas")
    
    # --- ZONA DE ACCIÓN RÁPIDA (PARA NO HACER 14 CLICS) ---
    with st.container():
        st.markdown("#### ⚡ Relleno Rápido (Ahorra tiempo)")
        c_tool1, c_tool2, c_tool3 = st.columns([2, 2, 1])
        
        with c_tool1:
            base_des = st.selectbox("Elegir Desayuno Base:", [r['nombre'] for r in RECETARIO['Desayunos']])
        with c_tool2:
            base_cen = st.selectbox("Elegir Cena Base:", [r['nombre'] for r in RECETARIO['Cenas']])
        with c_tool3:
            st.write("") # Espaciado
            st.write("") 
            if st.button("🚀 Aplicar a Toda la Semana"):
                st.session_state.menu_semanal["Desayuno"] = [base_des] * 7
                st.session_state.menu_semanal["Cena"] = [base_cen] * 7
                st.rerun() # Recarga la página para mostrar los cambios

    st.markdown("#### 📅 Ajuste Día por Día (Personaliza aquí)")
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    # Usamos un grid de 7 columnas para ver la semana completa
    cols = st.columns(7)
    
    for i, dia in enumerate(dias):
        with cols[i]:
            st.markdown(f"**{dia}**")
            
            # Buscamos el índice actual de la receta guardada en memoria
            # Esto permite que el selector "sepa" qué está seleccionado, ya sea por el botón rápido o manual
            try:
                idx_d = [r['nombre'] for r in RECETARIO['Desayunos']].index(st.session_state.menu_semanal["Desayuno"][i])
                idx_c = [r['nombre'] for r in RECETARIO['Cenas']].index(st.session_state.menu_semanal["Cena"][i])
            except ValueError:
                idx_d = 0
                idx_c = 0

            # Selector DESAYUNO
            new_d = st.selectbox(
                "Desayuno", 
                [r['nombre'] for r in RECETARIO['Desayunos']], 
                index=idx_d, 
                key=f"d_sel_{i}", 
                label_visibility="collapsed"
            )
            
            # Selector CENA
            new_c = st.selectbox(
                "Cena", 
                [r['nombre'] for r in RECETARIO['Cenas']], 
                index=idx_c, 
                key=f"c_sel_{i}", 
                label_visibility="collapsed"
            )
            
            # ACTUALIZACIÓN EN TIEMPO REAL
            # Si el usuario cambia este selector específico, actualizamos la memoria
            if new_d != st.session_state.menu_semanal["Desayuno"][i]:
                st.session_state.menu_semanal["Desayuno"][i] = new_d
                st.rerun()
            
            if new_c != st.session_state.menu_semanal["Cena"][i]:
                st.session_state.menu_semanal["Cena"][i] = new_c
                st.rerun()

# ==================================================
# PESTAÑA 2: AUDITORÍA DE CALORÍAS
# ==================================================
with tabs[1]:
    st.header("📊 Semáforo Nutricional")
    
    def get_macros(nombre):
        pool = RECETARIO['Almuerzos'] + RECETARIO['Desayunos'] + RECETARIO['Cenas']
        r = next((x for x in pool if x['nombre'] == nombre), None)
        return r['macros'] if r else {"cal":0, "prot":0}

    # Construimos la estructura de la semana
    semana_data = []
    for i, dia in enumerate(dias):
        # Lógica de almuerzo: Lun-Mie (alm_1), Jue-Vie (alm_2), Sab-Dom (alm_2 por defecto o sobras)
        almuerzo_actual = alm_1 if i < 3 else alm_2
        
        semana_data.append({
            "dia": dia,
            "des": st.session_state.menu_semanal["Desayuno"][i],
            "alm": almuerzo_actual,
            "cen": st.session_state.menu_semanal["Cena"][i]
        })

    col_e, col_c = st.columns(2)
    
    # AUDITORÍA EDIMAR
    with col_e:
        st.subheader("👩 Edimar (Meta ~2000-2200)")
        for d in semana_data:
            md = get_macros(d['des'])
            ma = get_macros(d['alm'])
            mc = get_macros(d['cen'])
            
            total_cal = (md['cal'] + ma['cal'] + mc['cal']) * f_e
            total_prot = (md['prot'] + ma['prot'] + mc['prot']) * f_e
            
            c1, c2 = st.columns([1, 2])
            c1.write(f"**{d['dia'][:3]}**")
            
            # Semáforo
            if total_cal < 1800:
                c2.error(f"{total_cal:.0f} kcal (Muy Bajo) 🚨")
            elif total_cal > 2500:
                c2.warning(f"{total_cal:.0f} kcal (Alto)")
            else:
                c2.success(f"{total_cal:.0f} kcal (Perfecto) ✅")
            
    # AUDITORÍA CARLOS
    with col_c:
        st.subheader("👨 Carlos (Meta ~2100-2400)")
        for d in semana_data:
            md = get_macros(d['des'])
            ma = get_macros(d['alm'])
            mc = get_macros(d['cen'])
            
            total_cal = (md['cal'] + ma['cal'] + mc['cal']) * f_c
            total_prot = (md['prot'] + ma['prot'] + mc['prot']) * f_c
            
            c1, c2 = st.columns([1, 2])
            c1.write(f"**{d['dia'][:3]}**")
            
            if total_cal < 1900:
                c2.error(f"{total_cal:.0f} kcal (Muy Bajo) 🚨")
            else:
                c2.success(f"{total_cal:.0f} kcal (Perfecto) ✅")

# ==================================================
# PESTAÑA 3: COMPRAS
# ==================================================
with tabs[2]:
    if st.button("🛒 Generar Lista de Compras", type="primary"):
        lista = {}
        
        def add_item(nombre, dias):
            pool = RECETARIO['Almuerzos'] + RECETARIO['Desayunos'] + RECETARIO['Cenas']
            r = next((x for x in pool if x['nombre'] == nombre), None)
            if r:
                for ing in r['ingredientes']:
                    key = ing['item']
                    pasillo = ing.get('pasillo', 'Otros')
                    # Fórmula maestra de cantidad
                    cant = (ing['cantidad'] * f_e + ing['cantidad'] * f_c) * dias
                    
                    if pasillo not in lista: lista[pasillo] = {}
                    if key not in lista[pasillo]: lista[pasillo][key] = 0
                    lista[pasillo][key] += cant

        # 1. Sumar Almuerzos Batch
        add_item(alm_1, 3) # Lun-Mie
        add_item(alm_2, 4) # Jue-Dom (Asumimos que comen de esto el finde)

        # 2. Sumar Desayunos y Cenas (Iterando los 7 días)
        for d in st.session_state.menu_semanal["Desayuno"]:
            add_item(d, 1)
        for c in st.session_state.menu_semanal["Cena"]:
            add_item(c, 1)

        # 3. Mostrar Resultados
        col1, col2 = st.columns(2)
        items = sorted(list(lista.items()))
        mitad = (len(items) // 2) + 1
        
        with col1:
            for pasillo, prods in items[:mitad]:
                with st.expander(pasillo, expanded=True):
                    for p, q in prods.items(): st.checkbox(f"{p}: {q:.0f}")
        with col2:
            for pasillo, prods in items[mitad:]:
                with st.expander(pasillo, expanded=True):
                    for p, q in prods.items(): st.checkbox(f"{p}: {q:.0f}")

# ==================================================
# PESTAÑA 4: COCINA
# ==================================================
with tabs[3]:
    st.header("👨‍🍳 Libro de Recetas")
    
    col_sel, col_view = st.columns([1, 2])
    
    with col_sel:
        st.markdown("**¿Qué quieres cocinar?**")
        cat = st.selectbox("Categoría", ["Almuerzos", "Desayunos", "Cenas"])
        plato = st.radio("Plato", [r['nombre'] for r in RECETARIO[cat]])
    
    with col_view:
        pool = RECETARIO['Almuerzos'] + RECETARIO['Desayunos'] + RECETARIO['Cenas']
        receta = next((x for x in pool if x['nombre'] == plato), None)
        
        if receta:
            st.markdown(f"## 📌 {receta['nombre']}")
            st.markdown(f"_{receta.get('descripcion', 'Sin descripción disponible')}_")
            
            # Info Nutricional
            m = receta['macros']
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Calorías Base", f"{m['cal']}")
            c2.metric("Proteína", f"{m['prot']}g")
            c3.metric("Carbos", f"{m['carb']}g")
            c4.metric("Grasas", f"{m['fat']}g")
            
            st.divider()
            
            # Ingredientes Dinámicos
            st.markdown("#### ⚖️ Cantidades (Ajustadas a tu peso)")
            df_ing = []
            for i in receta['ingredientes']:
                df_ing.append({
                    "Ingrediente": i['item'],
                    "Edimar": f"{i['cantidad']*f_e:.0f} {i['unidad']}",
                    "Carlos": f"{i['cantidad']*f_c:.0f} {i['unidad']}"
                })
            st.table(pd.DataFrame(df_ing))
            
            st.info(f"📝 **Instrucciones:**\n\n{receta['instrucciones']}")
