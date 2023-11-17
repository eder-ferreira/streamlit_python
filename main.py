from os import write
from numpy.core.fromnumeric import size
import streamlit as st
import Controllers.clienteController as clienteController
import Models.cliente as usuario
import pandas as pd

# CRIAR UM FORMULARIO STREAMLIT


st.sidebar.title("Menu")
opcao = st.sidebar.selectbox("CRUD", ["Cadastrar","Consultar","Alterar","Excluir"])

if opcao == 'Cadastrar':
    st.title("Cadastro de Usuário")
    with st.form(key="cadastrar_usuario"):
        nome_usuario = st.text_input(label="Digite o nome")
        email_usuario = st.text_input(label="Digite o email")
        senha_usuario = st.text_input(label="Digite o senha")
        ocupacao = st.selectbox("Selecione Aluno ou Professor",["Aluno","Professor","Admin"])
        dt_cadastro = st.date_input(label="Data do Cadastro:")
        enviar = st.form_submit_button("Enviar", type="primary")

    if enviar:
        usuario.nome_usuario = nome_usuario
        usuario.email_usuario = email_usuario
        usuario.senha_usuario = senha_usuario
        usuario.ocupacao = ocupacao
        usuario.dt_cadastro = dt_cadastro

        clienteController.cadastrar(usuario)
        st.success("Cadastro realizado com sucesso!")

elif opcao == 'Consultar':
    st.title("Consultar Usuário")
    userListe = []
    for item in clienteController.selecionar():
        userListe.append([item.nome_usuario,item.email_usuario,item.senha_usuario, item.ocupacao, item.dt_cadastro ])

    df = pd.DataFrame(
        userListe,
        columns=['nome_usuario', 'email_usuario', 'senha_usuario','ocupacao','dt_cadastro']
    )
    st.table(df)

