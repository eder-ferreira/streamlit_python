import streamlit as st
import Pages.Cliente.cadastrar as PageCadastrarUsuario
import Pages.Cliente.listar as PageConsultarUsuario
import Pages.Cliente.editar as PageEditarUsuario
import Pages.Cliente.excluir as PageExcluirUsuario
import Pages.Cliente.grafico as PageGrafico

import grafico_off

# CRIAR UM FORMULARIO STREAMLIT COM MENU CRUD
st.sidebar.title("Menu")
opcao = st.sidebar.selectbox('Opções', ['Cadastrar','Listar','Editar','Excluir','Dashboard'])

# INVOCA AS FUNÇÕES DO CRUD
if opcao == 'Cadastrar':
    PageCadastrarUsuario.cadastrar()

elif opcao == 'Listar':
    PageConsultarUsuario.listar()

elif opcao == 'Dashboard':
    PageGrafico.dados()

elif opcao == 'Editar':
    PageEditarUsuario.editar()

elif opcao == 'Excluir':
    PageExcluirUsuario.excluir(id)