import streamlit as st
import pandas as pd
 hotfix/mejoras_ui

st.title("Aplicación CSV Mejorada - Hotfix")

 


main

archivo = st.file_uploader("Sube un CSV", type=["csv"])

if archivo:
    df = pd.read_csv(archivo)
    st.dataframe(df, use_container_width=True)
    