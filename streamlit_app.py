import streamlit as st
import pandas as pd

st.title("Aplicación CSV Mejorada - Hotfix")

archivo = st.file_uploader("Sube un CSV", type=["csv"])

if archivo:
    df = pd.read_csv(archivo)
    st.experimental_data_editor(df, num_rows="dynamic")