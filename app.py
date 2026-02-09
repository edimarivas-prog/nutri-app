import streamlit as st
from recetas import RECETARIO

st.title("🍎 NutriApp: Edimar & Carlos")

# --- SECCIÓN DE PERFIL ---
st.sidebar.header("Tus Datos Actuales")
peso_edimar = st.sidebar.number_input("Peso Edimar (kg)", value=102.0)
peso_carlos = st.sidebar.number_input("Peso Carlos (kg)", value=81.0)

# Factor de ajuste: Si pesas 102kg, tu factor es 1.0. 
# Si bajas a 90kg, las porciones bajan proporcionalmente.
factor_edimar = peso_edimar / 102.0
factor_carlos = peso_carlos / 81.0

# --- SECCIÓN DE PLANIFICACIÓN ---
st.header("🗓️ Plan de la Semana")
opcion_a = st.selectbox("Almuerzo Lote A (Lun-Mie):", [r['nombre'] for r in RECETARIO['Almuerzos']])
opcion_b = st.selectbox("Almuerzo Lote B (Jue-Vie):", [r['nombre'] for r in RECETARIO['Almuerzos']])

# --- LÓGICA DE PORCIONES ---
if st.button("Generar Porciones y Lista"):
    st.subheader("🥣 Porciones para Edimar")
    # Aquí el código filtrará la receta elegida y multiplicará por factor_edimar
    st.write(f"Para el {opcion_a}, debes usar {round(180 * factor_edimar)}g de pollo.")

    st.subheader("🛒 Lista de Compras (Cantidades exactas)")
    # El sistema sumará (Porción Edimar * 5 días) + (Porción Carlos * 5 días)
    st.info("Suma total de pollo necesaria: 2.4 kg")
