import streamlit as st
import Controllers.clienteController as clienteController
from Models import cliente


def cadastrar():
    st.title(':blue[Cadastrar Usuarios] :computer:')
    with st.form(key="cadastrar_usuario"):
        nome_usuario = st.text_input(label="Digite o nome")
        email_usuario = st.text_input(label="Digite o email")
        senha_usuario = st.text_input(label="Digite o senha")
        ocupacao = st.selectbox("Selecione Aluno, Professor ou Admin",["Aluno","Professor","Admin"])
        dt_cadastro = st.date_input(label="Data do Cadastro:")
        enviar = st.form_submit_button("Enviar", type="primary")

    if enviar:
        clienteController.cadastrar(cliente.Cliente(0,nome_usuario,email_usuario,senha_usuario,ocupacao,dt_cadastro))
        st.success("Cadastro realizado com sucesso!")