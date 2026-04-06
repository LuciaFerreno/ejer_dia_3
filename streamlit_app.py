import streamlit as st
import pandas as pd

st.title("Aplicación CSV Mejorada - Hotfix")

archivo = st.file_uploader("Sube un CSV", type=["csv"])

if archivo:
    df = pd.read_csv(archivo)
    st.dataframe(df, use_container_width=True)
    