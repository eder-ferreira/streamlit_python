import streamlit as st
import Controllers.clienteController as clienteController
import pandas as pd

def consultar():
    st.title("Consultar Usuário")
    userListe = []
    for item in clienteController.selecionar():
        userListe.append([item.nome_usuario,item.email_usuario,item.senha_usuario, item.ocupacao, item.dt_cadastro ])

    df = pd.DataFrame(
        userListe,
        columns=['nome_usuario', 'email_usuario', 'senha_usuario','ocupacao','dt_cadastro']
    )
    st.table(df)