import streamlit as st
import pandas as pd

# Título de la app
st.title("Aplicación CSV Mejorada - Hotfix")

# Subir archivo CSV
archivo = st.file_uploader("Sube un CSV", type=["csv"])

# Mostrar la tabla editable si se sube un CSV
if archivo:
    df = pd.read_csv(archivo)
    st.experimental_data_editor(df, num_rows="dynamic")
    