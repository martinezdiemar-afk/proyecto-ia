import streamlit as st
import joblib
import numpy as np

# cargar modelo
model = joblib.load("modelo.pkl")

st.title("🎓 Sistema de Predicción de Rendimiento Académico")

st.write("Predicción de si el estudiante aprobará o suspenderá")

# inputs
studytime = st.number_input("Tiempo de estudio (1-4)", 1, 4)
failures = st.number_input("Suspensos anteriores", 0, 10)
absences = st.number_input("Faltas", 0, 100)

G1 = st.number_input("Nota G1", 0, 20)
G2 = st.number_input("Nota G2", 0, 20)

if st.button("Predecir resultado"):

    features = np.array([[studytime, failures, absences, G1, G2]])

    pred = model.predict(features)

    if pred[0] == 1:
        st.success("🟢 APROBADO")
    else:
        st.error("🔴 SUSPENDIDO")
