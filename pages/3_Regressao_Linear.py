import streamlit as st

st.set_page_config(
    layout="wide",
)

st.title("Regressao Linear Simples")
st.divider()

col_a1, col_a2 = st.columns(2)
with col_a1:
    st.image("reg.png", caption="Resultado da regressão")
with col_a2:
    st.markdown("""
        Como apenas a variável distância (*distance_km*) apresentou boa correlação com a variável alvo será feito primeiro uma
        regressão linear simples considerando apenas essa variável.
        
        A regressão foi realizada com o uso da biblioteca **SKLearn** e encontrou-se o seguinte resultado:
        
        #### Equação da Reta:
    """)
    st.latex(r"y \approx 0,8444x - 1,2735")
    st.markdown("""
        #### Erros do Ajuste:
        - MSE: $27,99$;
        - RMSE: $5,29$;
        - MAE: $2,57$;
    """)
    st.markdown("**Obs.:** Regressão múltipla abaixo.")

st.divider()
st.title("Regressão Linear Múltipla")
st.divider()

st.markdown("""
    Devido ao objetivo do trabalho (realizar uma regressão linear múltivariada) será feita uma regressão utilizando as variáveis
    distância (*distance_km*) e número de passageiros (*passenger_count*).
    
    A regressão foi realizada com o uso da biblioteca **SKLearn** e encontrou-se o seguinte resultado:

    #### Equação da Reta:
""")
st.latex(r"y \approx 0,8443x - 1,2713")
st.markdown("""
    #### Erros do Ajuste:
    - MSE: $28,00$;
    - RMSE: $5,29$;
    - MAE: $2,57$;
    
    **Obs.:** O gráfico dessa regressão não será plotado pois não é fácil compreender um gráfico de espalhamento e inclinações
    de reta em plotagens tridimensionais .
""")
