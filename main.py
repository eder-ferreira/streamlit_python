import streamlit as st
import Pages.Cliente.cadastrar as PageCadastrarUsuario
import Pages.Cliente.listar as PageConsultarUsuario
import Pages.Cliente.alterar as PageAlterarUsuario
import Pages.Cliente.excluir as PageExcluirUsuario
import grafico

# CRIAR UM FORMULARIO STREAMLIT COM MENU CRUD
st.sidebar.title("Menu")
opcao = st.sidebar.selectbox('Opções', ['Cadastrar','Listar','Alterar','Excluir','Dashboard'])

# INVOCA AS FUNÇÕES DO CRUD
if opcao == 'Cadastrar':
    PageCadastrarUsuario.cadastrar()

elif opcao == 'Listar':
    PageConsultarUsuario.listar()

elif opcao == 'Dashboard':
    grafico.grafico()

elif opcao == 'Alterar':
    PageAlterarUsuario.alterar()

elif opcao == 'Excluir':
    PageExcluirUsuario.excluir(id)