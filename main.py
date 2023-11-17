import streamlit as st
import Pages.Cliente.cadastrar as PageCadastrarUsuario
import Pages.Cliente.consultar as PageConsultarUsuario
import grafico

# CRIAR UM FORMULARIO STREAMLIT COM MENU CRUD
st.sidebar.title("Menu")
opcao = st.sidebar.selectbox("CRUD", ["Cadastrar","Consultar","Alterar","Excluir","Dashboard"])


# INVOCA AS FUNÇÕES DO CRUD
if opcao == 'Cadastrar':
    PageCadastrarUsuario.cadastrar()

if opcao == 'Consultar':
    PageConsultarUsuario.consultar()

if opcao == 'Dashboard':
    grafico.grafico()