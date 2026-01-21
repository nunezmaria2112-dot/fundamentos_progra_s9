import streamlit as st

st.title("Calculadora IMC")

st.sidebar.header("Parámetros")
peso = st.sidebar.number_input("Peso (KG)", 30, 300, value = None, placeholder = "Ingrese su peso")
estatura = st.sidebar.number_input("Estatura (CM)", 110, 250, value = None, placeholder = "Ingrese su estatura")

if st.button("Calcular"):
    estatura_m= estatura/100
    imc = peso / (estatura ** 2)
    st.metric(label="Su IMC es de: valuef*{imc:.2}")

    if imc < 25:
        st.succes("Rango óptimo")
    else:
        st.warning("Atención")