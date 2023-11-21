import streamlit as st
import Controllers.clienteController as clienteController
import pandas as pd


def listar():
    st.title(':blue[Listar Usuarios] :page_facing_up:')
    with st.form(key="listar_usuario"):
         userListe = []

    for item in clienteController.listar():
        userListe.append([item.id,item.nome_usuario,item.email_usuario,item.senha_usuario, item.ocupacao, item.dt_cadastro])

    df = pd.DataFrame(
        userListe,
        columns=['id', 'nome_usuario', 'email_usuario', 'senha_usuario','ocupacao','dt_cadastro']
    )

    st.table(df)