import streamlit as st
import pandas as pd
from recetas import RECETARIO

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="NutriPlan Pro", page_icon="🥗", layout="wide")

# Estilos CSS
st.markdown("""
    <style>
    .stSelectbox label { font-weight: bold; font-size: 1.1rem; color: #4CAF50; }
    div[data-testid="metric-container"] { background-color: #f0f2f6; border-radius: 8px; padding: 10px; }
    .stAlert { font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# --- INICIALIZAR ESTADO ---
if 'lista_compras' not in st.session_state:
    st.session_state.lista_compras = {}

# --- SIDEBAR: DATOS ---
with st.sidebar:
    st.header("📉 Tu Perfil")
    p_edimar = st.number_input("Peso Edimar (kg)", 60.0, 150.0, 102.0, 0.5)
    p_carlos = st.number_input("Peso Carlos (kg)", 60.0, 150.0, 81.0, 0.5)
    
    # Objetivo Calórico Mínimo (Para alertas)
    min_cal_e = 1800
    min_cal_c = 1900
    st.caption(f"⚠️ Alerta si Edimar come < {min_cal_e} kcal")

# Factores de Ajuste
f_e = p_edimar / 102.0
f_c = p_carlos / 81.0

# --- HEADER ---
st.title("🥗 NutriPlan: Auditoría de Macros")

# --- PESTAÑAS PRINCIPALES ---
# Reordenamos: Primero Planificar, Segundo Auditar Macros (Importante), Tercero Compras
tabs = st.tabs(["🗓️ 1. Planificar Menú", "📊 2. Auditoría de Macros", "🛒 3. Lista de Compras", "👨‍🍳 4. Cocinar"])

# ==================================================
# PESTAÑA 1: PLANIFICADOR (Lógica de Bloques)
# ==================================================
with tabs[0]:
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown("### 🍛 Almuerzos (Batch Cooking)")
        st.info("Lógica: Olla 1 para Lun-Mié | Olla 2 para Jue-Vie")
        alm_1 = st.selectbox("Almuerzo (Lun-Mié)", [r['nombre'] for r in RECETARIO['Almuerzos']], index=0)
        alm_2 = st.selectbox("Almuerzo (Jue-Vie)", [r['nombre'] for r in RECETARIO['Almuerzos']], index=1)
        st.caption("Sábados y Domingos se asume 'Libre' o 'Restos' en esta demo.")

    with c2:
        st.markdown("### ☀️ Desayunos y 🌙 Cenas")
        st.info("Lógica: Variar cada 3-4 días (No repetitivo, no diario)")
        
        col_bloque1, col_bloque2 = st.columns(2)
        
        with col_bloque1:
            st.markdown("**Bloque A (Lun - Jue)**")
            des_a = st.selectbox("Desayuno A", [r['nombre'] for r in RECETARIO['Desayunos']], index=0)
            cen_a = st.selectbox("Cena A", [r['nombre'] for r in RECETARIO['Cenas']], index=0)
            
        with col_bloque2:
            st.markdown("**Bloque B (Vie - Dom)**")
            des_b = st.selectbox("Desayuno B", [r['nombre'] for r in RECETARIO['Desayunos']], index=1)
            cen_b = st.selectbox("Cena B", [r['nombre'] for r in RECETARIO['Cenas']], index=1)

# ==================================================
# PESTAÑA 2: AUDITORÍA DE MACROS (NUEVO)
# ==================================================
with tabs[1]:
    st.header("📊 ¿Estamos comiendo suficiente?")
    st.markdown("Aquí sumamos **Desayuno + Almuerzo + Cena** de cada día para evitar comer menos de lo necesario.")

    # Función auxiliar para obtener macros de una receta
    def get_macros(nombre, tipo):
        # Busca en todas las listas
        pool = RECETARIO['Almuerzos'] + RECETARIO['Desayunos'] + RECETARIO['Cenas']
        r = next((x for x in pool if x['nombre'] == nombre), None)
        if r and 'macros' in r:
            return r['macros']
        return {"cal": 0, "prot": 0, "carb": 0, "fat": 0}

    # Construimos la semana simulada
    # Lun-Mie: Des A + Alm 1 + Cen A
    # Jue: Des A + Alm 2 + Cen A
    # Vie: Des B + Alm 2 + Cen B
    # Sab-Dom: Des B + (Asumimos Alm 2 o Libre) + Cen B -> Usaremos Alm 2 para calculo aprox
    
    dias_audit = [
        {"dia": "Lunes", "des": des_a, "alm": alm_1, "cen": cen_a},
        {"dia": "Martes", "des": des_a, "alm": alm_1, "cen": cen_a},
        {"dia": "Miércoles", "des": des_a, "alm": alm_1, "cen": cen_a},
        {"dia": "Jueves", "des": des_a, "alm": alm_2, "cen": cen_a}, # Cambio de Olla
        {"dia": "Viernes", "des": des_b, "alm": alm_2, "cen": cen_b}, # Cambio de Bloque
        {"dia": "Sábado", "des": des_b, "alm": alm_2, "cen": cen_b},
        {"dia": "Domingo", "des": des_b, "alm": alm_2, "cen": cen_b},
    ]

    # Mostrar Tabla
    col_e, col_c = st.columns(2)
    
    with col_e:
        st.subheader(f"👩 Edimar ({p_edimar} kg)")
        for d in dias_audit:
            m_d = get_macros(d['des'], 'Desayunos')
            m_a = get_macros(d['alm'], 'Almuerzos')
            m_c = get_macros(d['cen'], 'Cenas')
            
            # Suma Total Diaria ajustada al factor de Edimar
            total_cal = (m_d['cal'] + m_a['cal'] + m_c['cal']) * f_e
            total_prot = (m_d['prot'] + m_a['prot'] + m_c['prot']) * f_e
            
            # Renderizar fila
            with st.container(border=True):
                c_dia, c_cal, c_prot, c_alert = st.columns([1.5, 1.5, 1.5, 3])
                c_dia.markdown(f"**{d['dia']}**")
                c_cal.markdown(f"{total_cal:.0f} kcal")
                c_prot.markdown(f"prot: {total_prot:.0f}g")
                
                if total_cal < min_cal_e:
                    c_alert.error(f"⚠️ Bajo ({total_cal:.0f} < {min_cal_e})")
                elif total_cal > 2600:
                    c_alert.warning("⚠️ Alto")
                else:
                    c_alert.success("✅ Rango OK")

    with col_c:
        st.subheader(f"👨 Carlos ({p_carlos} kg)")
        for d in dias_audit:
            m_d = get_macros(d['des'], 'Desayunos')
            m_a = get_macros(d['alm'], 'Almuerzos')
            m_c = get_macros(d['cen'], 'Cenas')
            
            # Suma Total Diaria ajustada al factor de Carlos
            total_cal = (m_d['cal'] + m_a['cal'] + m_c['cal']) * f_c
            total_prot = (m_d['prot'] + m_a['prot'] + m_c['prot']) * f_c
            
            # Renderizar fila
            with st.container(border=True):
                c_dia, c_cal, c_prot, c_alert = st.columns([1.5, 1.5, 1.5, 3])
                c_dia.markdown(f"**{d['dia']}**")
                c_cal.markdown(f"{total_cal:.0f} kcal")
                c_prot.markdown(f"prot: {total_prot:.0f}g")
                
                if total_cal < min_cal_c:
                    c_alert.error(f"⚠️ Bajo ({total_cal:.0f} < {min_cal_c})")
                else:
                    c_alert.success("✅ Rango OK")

# ==================================================
# PESTAÑA 3: COMPRAS
# ==================================================
with tabs[2]:
    st.header("🛒 Lista de Supermercado")
    
    if st.button("Generar Lista Organizada", type="primary"):
        st.session_state.lista_compras = {} # Reiniciar

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

        # 1. Almuerzos
        agregar_smart(alm_1, 3) # Lun-Mie
        agregar_smart(alm_2, 2) # Jue-Vie
        
        # 2. Bloques A (4 días: Lun, Mar, Mie, Jue)
        agregar_smart(des_a, 4)
        agregar_smart(cen_a, 4)

        # 3. Bloques B (3 días: Vie, Sab, Dom)
        agregar_smart(des_b, 3)
        agregar_smart(cen_b, 3)

        # MOSTRAR
        col_a, col_b = st.columns(2)
        items_vista = list(st.session_state.lista_compras.items())
        mitad = (len(items_vista) // 2) + 1
        
        with col_a:
            for pasillo, items in items_vista[:mitad]:
                with st.container(border=True):
                    st.markdown(f"**{pasillo}**")
                    for ingrediente, cantidad in items.items():
                        st.checkbox(f"{ingrediente}: {cantidad:.0f}", key=f"{pasillo}_{ingrediente}")
        with col_b:
            for pasillo, items in items_vista[mitad:]:
                 with st.container(border=True):
                    st.markdown(f"**{pasillo}**")
                    for ingrediente, cantidad in items.items():
                        st.checkbox(f"{ingrediente}: {cantidad:.0f}", key=f"{pasillo}_{ingrediente}")

# ==================================================
# PESTAÑA 4: COCINA (CON MACROS DETALLADOS)
# ==================================================
with tabs[3]:
    st.header("👨‍🍳 Modo Cocina")
    opcion = st.selectbox("¿Qué cocinas hoy?", [
        "Olla 1 (Almuerzo Lun-Mié)", 
        "Olla 2 (Almuerzo Jue-Vie)", 
        "Desayuno Bloque A (Lun-Jue)",
        "Desayuno Bloque B (Vie-Dom)",
        "Cena Bloque A (Lun-Jue)",
        "Cena Bloque B (Vie-Dom)"
    ])
    
    # Mapeo de selección a receta
    if opcion == "Olla 1 (Almuerzo Lun-Mié)":
        receta_nombre, dias_factor = alm_1, 3
    elif opcion == "Olla 2 (Almuerzo Jue-Vie)":
        receta_nombre, dias_factor = alm_2, 2
    elif opcion == "Desayuno Bloque A (Lun-Jue)":
        receta_nombre, dias_factor = des_a, 1
    elif opcion == "Desayuno Bloque B (Vie-Dom)":
        receta_nombre, dias_factor = des_b, 1
    elif opcion == "Cena Bloque A (Lun-Jue)":
        receta_nombre, dias_factor = cen_a, 1
    else:
        receta_nombre, dias_factor = cen_b, 1

    pool = RECETARIO['Almuerzos'] + RECETARIO['Desayunos'] + RECETARIO['Cenas']
    receta = next((x for x in pool if x['nombre'] == receta_nombre), None)

    if receta:
        st.markdown(f"## 📌 {receta['nombre']}")
        
        # --- SECCIÓN MACROS REFORZADA ---
        st.markdown("### 🧬 Macros por Plato (Ajustado a tu peso)")
        col_m_e, col_m_c = st.columns(2)
        
        m = receta.get('macros', {'cal':0, 'prot':0})
        
        with col_m_e:
            st.info("👩 **Edimar**")
            st.write(f"**Calorías:** {m['cal']*f_e:.0f} kcal")
            st.write(f"**Proteína:** {m['prot']*f_e:.1f} g")

        with col_m_c:
            st.warning("👨 **Carlos**")
            st.write(f"**Calorías:** {m['cal']*f_c:.0f} kcal")
            st.write(f"**Proteína:** {m['prot']*f_c:.1f} g")

        st.markdown("---")
        st.markdown("### 🥘 Ingredientes")
        
        # Tabla simple
        data = []
        for i in receta['ingredientes']:
            data.append({
                "Ingrediente": i['item'],
                "Total Olla": f"{(i['cantidad']*(f_e+f_c)*dias_factor):.0f} {i['unidad']}",
                "Tu Plato (Edimar)": f"{(i['cantidad']*f_e):.0f}",
                "Su Plato (Carlos)": f"{(i['cantidad']*f_c):.0f}"
            })
        st.table(pd.DataFrame(data))
        
        st.markdown("### 📝 Instrucciones")
        st.write(receta['instrucciones'])
