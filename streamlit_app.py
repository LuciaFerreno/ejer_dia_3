import streamlit as st
import pandas as pd
 
st.title("¡Hola, mundo!")


archivo = st.file_uploader("Sube un CSV", type=["csv"])

if archivo:
    df = pd.read_csv(archivo)
    st.dataframe(df)