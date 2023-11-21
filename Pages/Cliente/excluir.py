import streamlit as st
import Controllers.clienteController as clienteController
import pandas as pd


def excluir(id):
    st.title(':red[Excluir Usuarios] :wastebasket:')
    with st.form(key="excluir_usuario"):
        id = st.text_input(label="Insira o Id a ser excluido:")
        btExcluir = st.form_submit_button("Excluir", type="primary")

    userListe = []
    for item in clienteController.listar():
        userListe.append([item.id,item.nome_usuario,item.email_usuario,item.senha_usuario, item.ocupacao, item.dt_cadastro])

    df = pd.DataFrame(
        userListe,
        columns=['id', 'nome_usuario', 'email_usuario', 'senha_usuario','ocupacao','dt_cadastro']
    )
    st.table(df)

    if btExcluir:
        clienteController.excluir(id)
        st.success(f'Id: {id} excluido com sucesso!')