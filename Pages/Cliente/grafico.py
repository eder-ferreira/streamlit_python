import streamlit as st      # BIBLIOTECA CONSTRUIR OS DASHBOARD
import pandas as pd         # BIBLIOTECA MANIPULAÇÃO DE DADOS
# import plotly.express as px # BIBLIOTECA CONSTRUIR OS GRAFICOS
import Controllers.clienteController as clienteController


# RECUPERA DADOS DA TABELA ESTOQUE PRODUTOS
def dados():
    st.title('Base dados :blue[Estoque] :bar_chart:')
    with st.form(key='dashboard'):
        userListe = []
    for item in clienteController.carregar_dados():
        userListe.append([item.id, item.descricao, item.quantidade, item.valor, item.dt_cadastro])

    df = pd.DataFrame(
        userListe,
        columns=['id', 'descricao', 'quantidade', 'valor','dt_cadastro']
    )
    st.table(df)

# SELEÇÃO
    selecao = st.selectbox("Gerar Gráfico?", ["Não", "Sim"])
    if selecao == "Sim":
        st.title(':blue[Estoque por Produto x Quantidade]')

        col1, col2 = st.columns(2)
        col3, col4, col5 = st.columns(3)

        grafico = px.bar(userListe,x=1, y=2)
        col3.plotly_chart(grafico, use_container_width=False)

        with col1:
            st.write("""
            Estes dados são extraidos do banco de dados da academia!
            """)
        with col2:
            st.write("""
            E utilizados para compor a base de dados do estoque atual dos produtos comercializados.
            """)

        st.title(':blue[Produto x Quantidade]')
        col1, col2 = st.columns(2)
        col3, col4, col5 = st.columns(3)

        pizza = px.pie(userListe, values=0, names=1)
        col4.plotly_chart(pizza, use_container_width=False)


