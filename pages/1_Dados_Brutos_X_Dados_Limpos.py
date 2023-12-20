import streamlit as st
import plotly.express as px
import pandas as pd

# Pandas

uber = pd.read_csv("uber_distancia.csv")
uber_final = pd.read_csv("uber_final.csv")

# Streamlit

st.set_page_config(
    layout="wide",
)

st.title("Dados Brutos X Dados Limpos")

st.divider()

st.header("Dados Brutos")

col_a1, col_a2 = st.columns(2)
with col_a1:
    st.subheader("Distância")
    hist_distancia = px.histogram(uber, x="distance_km")
    st.plotly_chart(hist_distancia, use_container_width=True)

with col_a2:
    st.subheader("Distância X Preço")
    dist_x_preco = px.scatter(uber, x="distance_km", y="fare_amount")
    st.plotly_chart(dist_x_preco, use_container_width=True)

st.header("Dados Limpos")

col_b1, col_b2 = st.columns(2)
with col_b1:
    st.subheader("Distância")
    hist_distancia2 = px.histogram(uber_final, x="distance_km")
    st.plotly_chart(hist_distancia2, use_container_width=True)

with col_b2:
    st.subheader("Distância X Preço")
    dist_x_preco2 = px.scatter(uber_final, x="distance_km", y="fare_amount")
    st.plotly_chart(dist_x_preco2, use_container_width=True)

