import streamlit as st
import joblib
import numpy as np


model = joblib.load("modelo.pkl")

st.title("🎓 Predicción de Nota Final (G3)")

st.write("Introduce los datos del estudiante:")

studytime = st.number_input("Tiempo de estudio (1-4)", min_value=1, max_value=4)
failures = st.number_input("Número de suspensos anteriores", min_value=0, max_value=10)
absences = st.number_input("Faltas de asistencia", min_value=0, max_value=100)

G1 = st.number_input("Nota G1", min_value=0, max_value=20)
G2 = st.number_input("Nota G2", min_value=0, max_value=20)


if st.button("Predecir G3"):
    
    features = np.array([[studytime, failures, absences, G1, G2]])
    
    pred = model.predict(features)

    st.success(f"🎯 Nota final estimada (G3): {pred[0]:.2f}")
