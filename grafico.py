import streamlit as st
import pandas as pd

@st.cache_data
def carregar_dados():
    tabela = pd.read_csv("resultados.csv")
    return tabela

def grafico():
        qtde_dias = st.selectbox("Selecione o período", ["7D", "15D", "21D", "30D"])
        num_dias = int(qtde_dias.replace("D", ""))
        dados = carregar_dados()
        dados = dados[-num_dias:]
        st.area_chart(dados, x="Data", y="Contratos")