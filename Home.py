import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="AT - Projeto de Bloco",
)

st.title("AT - Projeto de Bloco")

st.divider()

st.header("Resumo do Trabalho")

st.markdown("""
    Este trabalho busca prever o preço de uma corrida de Uber através de uma regressão linear com base nos dados obtidos
    pelo dataset Uber-Fares (*https://www.kaggle.com/datasets/yasserh/uber-fares-dataset*) da plataforma Kaggle.
""")

st.divider()

st.markdown("""
    *Giuliano Mantovi*
    *Disciplina Projeto de Bloco, Instituto INFNET.*
""")