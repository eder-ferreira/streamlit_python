from os import write
from numpy.core.fromnumeric import size
import streamlit as st
import Controllers.clienteController as clienteController
import Models.cliente as usuario
import datetime as date

# CRIAR UM FORMULARIO STREAMLIT
st.title("Tela de login")
with st.form(key="cadastrar_usuario"):
    nome_usuario = st.text_input(label="Digite o nome")
    email_usuario = st.text_input(label="Digite o email")
    senha_usuario = st.text_input(label="Digite o senha")
    ocupacao = st.selectbox("Selecione Aluno ou Professor",["Aluno","Professor"])
    # dt_cadastro = st.date_input(date.datetime)
    enviar = st.form_submit_button("Enviar")

# VERIFICA SE ESTÁ CAPTURANDO
#     st.write(f"Nome: {nome_usuario}")
#     st.write(f"E-mail: {email_usuario}")
#     st.write(f"Senha: {senha_usuario}")
#     st.write(f"Ocupação: {ocupacao}")

if enviar:
    usuario.nome_usuario = nome_usuario
    usuario.email_usuario = email_usuario
    usuario.senha_usuario = senha_usuario
    usuario.ocupacao = ocupacao
    # usuario.dt_cadastro = dt_cadastro

    clienteController.cadastrar(usuario)




