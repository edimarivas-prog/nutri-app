import streamlit as st
import pandas as pd
from recetas_mejoradas import RECETARIO

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="NutriPlan Pro", page_icon="💪", layout="wide")

# --- CONSTANTES ---
META_CALORIAS_EDIMAR = 2200
META_PROTEINA_EDIMAR = 140
META_CALORIAS_CARLOS = 2400
META_PROTEINA_CARLOS = 160

# Estilos mejorados
st.markdown("""
    <style>
    .stSelectbox label { font-size: 0.9rem; font-weight: bold; color: #4CAF50; }
    .block-container { padding-top: 2rem; }
    div[data-testid="column"] { 
        background-color: #f9f9f9; 
        padding: 15px; 
        border-radius: 10px; 
        border: 1px solid #eee;
    }
    .metric-card {
        background: white;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 5px 0;
    }
    .alerta-macro {
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
        font-weight: bold;
    }
    .alerta-ok { background-color: #d4edda; color: #155724; }
    .alerta-bajo { background-color: #fff3cd; color: #856404; }
    .alerta-alto { background-color: #f8d7da; color: #721c24; }
    </style>
""", unsafe_allow_html=True)

# --- MEMORIA (SESSION STATE) ---
if 'menu_semanal' not in st.session_state:
    st.session_state.menu_semanal = {
        "Desayuno": [RECETARIO['Desayunos'][0]['nombre']] * 7,
        "Almuerzo": [RECETARIO['Almuerzos'][0]['nombre']] * 7,
        "Cena": [RECETARIO['Cenas'][0]['nombre']] * 7
    }

# --- FUNCIONES AUXILIARES ---
def get_receta(nombre):
    """Busca una receta en todo el recetario"""
    for categoria in ['Desayunos', 'Almuerzos', 'Cenas', 'Meriendas']:
        for receta in RECETARIO.get(categoria, []):
            if receta['nombre'] == nombre:
                return receta
    return None

def calcular_macros_dia(dia_idx, factor_peso):
    """Calcula macros totales de un día"""
    des = st.session_state.menu_semanal["Desayuno"][dia_idx]
    alm = st.session_state.menu_semanal["Almuerzo"][dia_idx]
    cen = st.session_state.menu_semanal["Cena"][dia_idx]
    
    total = {"cal": 0, "prot": 0, "carb": 0, "fat": 0}
    
    for nombre in [des, alm, cen]:
        receta = get_receta(nombre)
        if receta:
            for key in total.keys():
                total[key] += receta['macros'].get(key, 0) * factor_peso
    
    return total

def validar_meta(valor, meta, tolerancia=0.15):
    """Valida si un valor está dentro de la meta ±tolerancia"""
    min_val = meta * (1 - tolerancia)
    max_val = meta * (1 + tolerancia)
    if valor < min_val:
        return "bajo"
    elif valor > max_val:
        return "alto"
    else:
        return "ok"

# --- BARRA LATERAL ---
with st.sidebar:
    st.header("⚙️ Configuración Personal")
    
    st.subheader("👩 Edimar")
    p_edimar = st.number_input("Peso (kg)", 60.0, 150.0, 102.0, 0.5, key="peso_e")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Meta Calorías", f"{META_CALORIAS_EDIMAR}")
    with col2:
        st.metric("Meta Proteína", f"{META_PROTEINA_EDIMAR}g")
    
    st.divider()
    
    st.subheader("👨 Carlos")
    p_carlos = st.number_input("Peso (kg)", 60.0, 150.0, 81.0, 0.5, key="peso_c")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Meta Calorías", f"{META_CALORIAS_CARLOS}")
    with col2:
        st.metric("Meta Proteína", f"{META_PROTEINA_CARLOS}g")
    
    st.markdown("---")
    st.info("💡 **Tip:** La app ajusta automáticamente las porciones según tu peso actual.")

# Factores de ajuste
f_e = p_edimar / 102.0
f_c = p_carlos / 81.0

# --- TÍTULO ---
st.title("💪 NutriPlan Pro: Planificación Inteligente")

# --- PESTAÑAS ---
tabs = st.tabs(["📊 Dashboard", "🗓️ Planificador", "📖 Recetario", "🛒 Lista de Compras"])

# ==================================================
# PESTAÑA 1: DASHBOARD NUTRICIONAL
# ==================================================
with tabs[0]:
    st.header("📊 Análisis Nutricional Semanal")
    
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    # ANÁLISIS EDIMAR
    st.subheader("👩 Edimar - Seguimiento Semanal")
    
    datos_edimar = []
    for i, dia in enumerate(dias):
        macros = calcular_macros_dia(i, f_e)
        datos_edimar.append({
            "Día": dia,
            "Calorías": f"{macros['cal']:.0f}",
            "Proteína": f"{macros['prot']:.0f}g",
            "Carbos": f"{macros['carb']:.0f}g",
            "Grasas": f"{macros['fat']:.0f}g",
            "Estado Cal": validar_meta(macros['cal'], META_CALORIAS_EDIMAR),
            "Estado Prot": validar_meta(macros['prot'], META_PROTEINA_EDIMAR)
        })
    
    df_edimar = pd.DataFrame(datos_edimar)
    
    # Mostrar tabla con colores
    col1, col2 = st.columns([3, 1])
    with col1:
        st.dataframe(df_edimar[["Día", "Calorías", "Proteína", "Carbos", "Grasas"]], 
                    use_container_width=True, hide_index=True)
    
    with col2:
        # Resumen semanal
        cal_promedio = sum([calcular_macros_dia(i, f_e)['cal'] for i in range(7)]) / 7
        prot_promedio = sum([calcular_macros_dia(i, f_e)['prot'] for i in range(7)]) / 7
        
        st.metric("Promedio Calorías", f"{cal_promedio:.0f}", 
                 delta=f"{cal_promedio - META_CALORIAS_EDIMAR:.0f}")
        st.metric("Promedio Proteína", f"{prot_promedio:.0f}g",
                 delta=f"{prot_promedio - META_PROTEINA_EDIMAR:.0f}g")
    
    # Alertas
    dias_problema = [d for d in datos_edimar if d['Estado Cal'] != 'ok' or d['Estado Prot'] != 'ok']
    if dias_problema:
        st.warning(f"⚠️ {len(dias_problema)} días necesitan ajuste")
        for d in dias_problema:
            if d['Estado Cal'] == 'bajo':
                st.markdown(f"🔸 **{d['Día']}**: Calorías bajas ({d['Calorías']})")
            if d['Estado Prot'] == 'bajo':
                st.markdown(f"🔸 **{d['Día']}**: Proteína baja ({d['Proteína']})")
    else:
        st.success("✅ Toda la semana cumple con los objetivos")
    
    st.divider()
    
    # ANÁLISIS CARLOS
    st.subheader("👨 Carlos - Seguimiento Semanal")
    
    datos_carlos = []
    for i, dia in enumerate(dias):
        macros = calcular_macros_dia(i, f_c)
        datos_carlos.append({
            "Día": dia,
            "Calorías": f"{macros['cal']:.0f}",
            "Proteína": f"{macros['prot']:.0f}g",
            "Carbos": f"{macros['carb']:.0f}g",
            "Grasas": f"{macros['fat']:.0f}g",
        })
    
    df_carlos = pd.DataFrame(datos_carlos)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.dataframe(df_carlos[["Día", "Calorías", "Proteína", "Carbos", "Grasas"]], 
                    use_container_width=True, hide_index=True)
    
    with col2:
        cal_promedio_c = sum([calcular_macros_dia(i, f_c)['cal'] for i in range(7)]) / 7
        prot_promedio_c = sum([calcular_macros_dia(i, f_c)['prot'] for i in range(7)]) / 7
        
        st.metric("Promedio Calorías", f"{cal_promedio_c:.0f}", 
                 delta=f"{cal_promedio_c - META_CALORIAS_CARLOS:.0f}")
        st.metric("Promedio Proteína", f"{prot_promedio_c:.0f}g",
                 delta=f"{prot_promedio_c - META_PROTEINA_CARLOS:.0f}g")

# ==================================================
# PESTAÑA 2: PLANIFICADOR
# ==================================================
with tabs[1]:
    st.subheader("🗓️ Planificador Semanal de Comidas")
    
    # Herramienta de relleno rápido
    with st.expander("⚡ Relleno Rápido - Aplicar misma comida a toda la semana", expanded=False):
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            quick_des = st.selectbox("Desayuno base:", 
                                    [r['nombre'] for r in RECETARIO['Desayunos']], 
                                    key="quick_des")
        with col2:
            quick_alm = st.selectbox("Almuerzo base:", 
                                    [r['nombre'] for r in RECETARIO['Almuerzos']], 
                                    key="quick_alm")
        with col3:
            quick_cen = st.selectbox("Cena base:", 
                                    [r['nombre'] for r in RECETARIO['Cenas']], 
                                    key="quick_cen")
        with col4:
            st.write("")
            st.write("")
            if st.button("🚀 Aplicar a toda la semana", type="primary"):
                st.session_state.menu_semanal["Desayuno"] = [quick_des] * 7
                st.session_state.menu_semanal["Almuerzo"] = [quick_alm] * 7
                st.session_state.menu_semanal["Cena"] = [quick_cen] * 7
                st.rerun()
    
    st.markdown("---")
    st.markdown("### 📅 Planificación Día por Día")
    
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    # Crear columnas para cada día
    cols = st.columns(7)
    
    for i, dia in enumerate(dias):
        with cols[i]:
            st.markdown(f"**{dia}**")
            
            # Calcular macros del día para preview
            macros_dia = calcular_macros_dia(i, f_e)
            estado_cal = validar_meta(macros_dia['cal'], META_CALORIAS_EDIMAR)
            
            # Indicador visual
            if estado_cal == "ok":
                st.markdown("🟢")
            elif estado_cal == "bajo":
                st.markdown("🟡")
            else:
                st.markdown("🔴")
            
            # Desayuno
            try:
                idx_d = [r['nombre'] for r in RECETARIO['Desayunos']].index(
                    st.session_state.menu_semanal["Desayuno"][i])
            except:
                idx_d = 0
            
            new_d = st.selectbox("🌅", 
                                [r['nombre'] for r in RECETARIO['Desayunos']], 
                                index=idx_d, 
                                key=f"d_{i}",
                                label_visibility="collapsed")
            
            # Almuerzo
            try:
                idx_a = [r['nombre'] for r in RECETARIO['Almuerzos']].index(
                    st.session_state.menu_semanal["Almuerzo"][i])
            except:
                idx_a = 0
            
            new_a = st.selectbox("🍛", 
                                [r['nombre'] for r in RECETARIO['Almuerzos']], 
                                index=idx_a, 
                                key=f"a_{i}",
                                label_visibility="collapsed")
            
            # Cena
            try:
                idx_c = [r['nombre'] for r in RECETARIO['Cenas']].index(
                    st.session_state.menu_semanal["Cena"][i])
            except:
                idx_c = 0
            
            new_c = st.selectbox("🌙", 
                                [r['nombre'] for r in RECETARIO['Cenas']], 
                                index=idx_c, 
                                key=f"c_{i}",
                                label_visibility="collapsed")
            
            # Preview de macros
            st.caption(f"{macros_dia['cal']:.0f} kcal")
            st.caption(f"{macros_dia['prot']:.0f}g prot")
            
            # Actualizar si cambió
            if new_d != st.session_state.menu_semanal["Desayuno"][i]:
                st.session_state.menu_semanal["Desayuno"][i] = new_d
                st.rerun()
            if new_a != st.session_state.menu_semanal["Almuerzo"][i]:
                st.session_state.menu_semanal["Almuerzo"][i] = new_a
                st.rerun()
            if new_c != st.session_state.menu_semanal["Cena"][i]:
                st.session_state.menu_semanal["Cena"][i] = new_c
                st.rerun()

# ==================================================
# PESTAÑA 3: RECETARIO COMPLETO
# ==================================================
with tabs[2]:
    st.header("📖 Libro de Recetas Completo")
    
    col_filtro, col_contenido = st.columns([1, 3])
    
    with col_filtro:
        st.subheader("Filtros")
        categoria_sel = st.radio("Categoría", 
                                ["Todos", "Desayunos", "Almuerzos", "Cenas", "Meriendas"])
        
        # Filtro de calorías
        st.markdown("---")
        st.markdown("**Rango de Calorías**")
        cal_min = st.number_input("Min", 0, 1500, 0, 50)
        cal_max = st.number_input("Max", 0, 1500, 1500, 50)
        
        # Filtro de proteína
        st.markdown("**Proteína Mínima**")
        prot_min = st.number_input("Gramos", 0, 100, 0, 5)
    
    with col_contenido:
        # Construir lista de recetas filtradas
        recetas_mostrar = []
        
        if categoria_sel == "Todos":
            categorias = ["Desayunos", "Almuerzos", "Cenas", "Meriendas"]
        else:
            categorias = [categoria_sel]
        
        for cat in categorias:
            for receta in RECETARIO.get(cat, []):
                # Aplicar filtros
                calorias = receta['macros']['cal']
                proteina = receta['macros']['prot']
                
                if (cal_min <= calorias <= cal_max and 
                    proteina >= prot_min):
                    recetas_mostrar.append({
                        "categoria": cat,
                        "receta": receta
                    })
        
        st.markdown(f"### {len(recetas_mostrar)} recetas encontradas")
        
        # Mostrar recetas en grid
        for item in recetas_mostrar:
            receta = item['receta']
            cat = item['categoria']
            
            with st.expander(f"**{receta['nombre']}** ({cat})", expanded=False):
                # Macros principales
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("🔥 Calorías", f"{receta['macros']['cal']}")
                col2.metric("💪 Proteína", f"{receta['macros']['prot']}g")
                col3.metric("🍞 Carbos", f"{receta['macros']['carb']}g")
                col4.metric("🥑 Grasas", f"{receta['macros']['fat']}g")
                
                # Descripción
                if 'descripcion' in receta:
                    st.markdown(f"*{receta['descripcion']}*")
                
                st.markdown("---")
                
                # Ingredientes
                col_ing, col_inst = st.columns(2)
                
                with col_ing:
                    st.markdown("**📝 Ingredientes (por persona base)**")
                    for ing in receta['ingredientes']:
                        st.markdown(f"- {ing['cantidad']} {ing['unidad']} {ing['item']}")
                
                with col_inst:
                    st.markdown("**👨‍🍳 Preparación**")
                    st.markdown(receta['instrucciones'])
                
                # Cantidades ajustadas
                st.markdown("---")
                st.markdown("**⚖️ Cantidades Ajustadas a Peso Actual**")
                
                col_e, col_c = st.columns(2)
                
                with col_e:
                    st.markdown("**Edimar:**")
                    for ing in receta['ingredientes']:
                        cant_ajustada = ing['cantidad'] * f_e
                        st.caption(f"• {cant_ajustada:.0f} {ing['unidad']} {ing['item']}")
                
                with col_c:
                    st.markdown("**Carlos:**")
                    for ing in receta['ingredientes']:
                        cant_ajustada = ing['cantidad'] * f_c
                        st.caption(f"• {cant_ajustada:.0f} {ing['unidad']} {ing['item']}")

# ==================================================
# PESTAÑA 4: LISTA DE COMPRAS
# ==================================================
with tabs[3]:
    st.header("🛒 Lista de Compras Semanal")
    
    if st.button("🔄 Generar Lista Actualizada", type="primary"):
        lista_compras = {}
        
        # Función para agregar ingredientes
        def agregar_ingredientes(nombre_receta, cantidad_veces):
            receta = get_receta(nombre_receta)
            if not receta:
                return
            
            for ing in receta['ingredientes']:
                pasillo = ing.get('pasillo', 'Otros')
                item = ing['item']
                
                # Calcular cantidad total (Edimar + Carlos) * veces que se usa
                cantidad_total = (ing['cantidad'] * f_e + ing['cantidad'] * f_c) * cantidad_veces
                unidad = ing['unidad']
                
                if pasillo not in lista_compras:
                    lista_compras[pasillo] = {}
                
                if item not in lista_compras[pasillo]:
                    lista_compras[pasillo][item] = {'cantidad': 0, 'unidad': unidad}
                
                lista_compras[pasillo][item]['cantidad'] += cantidad_total
        
        # Contar frecuencia de cada receta
        contador_recetas = {}
        
        for dia in range(7):
            for tiempo in ["Desayuno", "Almuerzo", "Cena"]:
                receta_nombre = st.session_state.menu_semanal[tiempo][dia]
                if receta_nombre not in contador_recetas:
                    contador_recetas[receta_nombre] = 0
                contador_recetas[receta_nombre] += 1
        
        # Agregar ingredientes según frecuencia
        for receta_nombre, veces in contador_recetas.items():
            agregar_ingredientes(receta_nombre, veces)
        
        # Mostrar lista organizada por pasillo
        pasillos_ordenados = sorted(lista_compras.keys())
        
        # Dividir en dos columnas
        col1, col2 = st.columns(2)
        mitad = len(pasillos_ordenados) // 2
        
        with col1:
            for pasillo in pasillos_ordenados[:mitad]:
                with st.expander(f"**{pasillo}**", expanded=True):
                    items = lista_compras[pasillo]
                    for item, datos in sorted(items.items()):
                        cantidad = datos['cantidad']
                        unidad = datos['unidad']
                        checked = st.checkbox(
                            f"{item}: {cantidad:.0f} {unidad}", 
                            key=f"check_{pasillo}_{item}"
                        )
        
        with col2:
            for pasillo in pasillos_ordenados[mitad:]:
                with st.expander(f"**{pasillo}**", expanded=True):
                    items = lista_compras[pasillo]
                    for item, datos in sorted(items.items()):
                        cantidad = datos['cantidad']
                        unidad = datos['unidad']
                        checked = st.checkbox(
                            f"{item}: {cantidad:.0f} {unidad}", 
                            key=f"check_{pasillo}_{item}"
                        )
        
        # Resumen
        st.markdown("---")
        total_items = sum([len(items) for items in lista_compras.values()])
        st.info(f"📦 Total de items: **{total_items}** productos diferentes")
        
        # Botón para descargar
        st.download_button(
            label="📄 Descargar lista (texto)",
            data=generar_texto_lista(lista_compras),
            file_name="lista_compras.txt",
            mime="text/plain"
        )

def generar_texto_lista(lista):
    """Genera texto plano de la lista de compras"""
    texto = "LISTA DE COMPRAS - NUTRIPLAN PRO\n"
    texto += "=" * 50 + "\n\n"
    
    for pasillo, items in sorted(lista.items()):
        texto += f"\n{pasillo}\n"
        texto += "-" * len(pasillo) + "\n"
        for item, datos in sorted(items.items()):
            texto += f"[ ] {item}: {datos['cantidad']:.0f} {datos['unidad']}\n"
    
    return texto
