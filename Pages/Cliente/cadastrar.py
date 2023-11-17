import streamlit as st
import Controllers.clienteController as clienteController
import Models.cliente as usuario

def cadastrar():
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