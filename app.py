import streamlit as st
import joblib
import numpy as np

# Configuración página
st.set_page_config(
    page_title="Predicción Académica EPSA",
    page_icon="🎓",
    layout="centered"
)

# cargar modelo
model = joblib.load("modelo.pkl")

# título
st.title("🎓 Sistema Inteligente de Predicción Académica")
st.markdown("### Escuela Politécnica Superior de Alcoy")

st.write(
    "Esta aplicación predice si un estudiante aprobará o suspenderá "
    "utilizando técnicas de Machine Learning."
)

st.divider()

# inputs
st.subheader("📋 Datos del estudiante")

studytime = st.slider("Tiempo de estudio", 1, 4, 2)

failures = st.number_input(
    "Número de suspensos anteriores",
    min_value=0,
    max_value=10,
    value=0
)

absences = st.number_input(
    "Número de faltas",
    min_value=0,
    max_value=100,
    value=0
)

G1 = st.slider("Nota G1", 0, 20, 10)
G2 = st.slider("Nota G2", 0, 20, 10)

st.divider()

# botón
if st.button("🔍 Predecir resultado"):

    features = np.array([[studytime, failures, absences, G1, G2]])

    pred = model.predict(features)

    if pred[0] == 1:
        st.success("🟢 El estudiante probablemente APROBARÁ")
        st.balloons()

    else:
        st.error("🔴 El estudiante presenta riesgo de SUSPENSO")

st.divider()

st.caption("Proyecto de Machine Learning - EPSA")
