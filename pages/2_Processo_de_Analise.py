import streamlit as st

st.set_page_config(
    layout="wide",
)

st.title("Processo de Análise")
st.divider()

st.markdown("""
    ## 1 - Cálculo das Distâncias
    
    As distâncias de cada viagem foram calculadas com base na latitude e longitude de partida (*pickup_latitude* e *pickup_longitude*)
     e de chegada (*dropoff_latitude* e *dropoff_longitude*) utilizando a biblioteca **Geopy**.
""")

codigo = """from geopy import distance

distancias = []
for _, row in uber_ok.iterrows():
    inicio = (row["pickup_latitude"], row["pickup_longitude"])
    fim = (row["dropoff_latitude"], row["dropoff_longitude"])
    
    distancia = distance.distance(inicio, fim).km
    distancias.append(distancia)
"""

st.code(codigo)

st.markdown("""
    ## 2 - Identificação de Viagens Válidas
    
    Após calcular as distância foi feita uma verificação para determinar quais viagens seriam consideradas válidas.
    
    Os critérios para uma viagem ser considerada válida foram:
    
    1. Distância entre 0 e 100 Km, pois toda distância deve ser positiva e não é comum que viagens de Uber percorram distâncias muito grandes;
    2. Número de passageiros menor que 5, pois em um carro cabe apenas 4 passageiros (desconsiderando o motorista).
""")

st.markdown("""
    ## 3 - Identificação de Outliers
    
    ### Colunas de Latitude e Longitude
    As colunas referentes as latitudes e longitudes foram ignoradas na verificação de outliers pois não apresentam nenhuma
    informação relevante para a regressão linear (com exceção para o cálculo das distâncias).
    
    ### Coluna Distância
""")

st.image("../plots/distance_plot.png")

st.markdown("""
    Através do cálculo dos outliers foram encontrados um limite superior de 7,8 Km e um limite inferior de -2,7 Km.
    Os outliers foram considerados pois é possível que uma viagem de Uber ultrapasse o limite superior e por que não existem
    valores negativos nessa coluna.
    
    ### Coluna Passageiros
""")

st.image("../plots/passenger_plot.png")
st.markdown("""
    Todos os valores encontrados no histograma ou no boxplot são possíveis para o número de passageiros de uma viagem portanto
    os outliers serão considerados no cálculo da regressão.

    ### Coluna Preço
""")

st.markdown("""
    Com o cálculo dos outliers foram encontrados um limite superior de 22.25 USD e um limite inferior de -3,75 USD. Os outliers
    foram considerados.
    
    #### Relacionando a Coluna Preço com a Coluna Distância
    
    Pelos gráficos abaixo percebe-se que existem viagens com distâncias grandes e valor muito baixo assim como viagens com
    valores muito altos para distâncias pequenas.
    
    Essas viagens foram desconsideradas.
""")
col_a1, col_a2 = st.columns(2)
with col_a1:
    st.image("../plots/fare_scatter_1.png", caption="Preço X Distância (Antes da Limpeza)")
with col_a2:
    st.image("../plots/fare_scatter_2.png", caption="Preço X Distância (Depois da Limpeza)")

st.markdown("""
    ## 4 - Análise de Correlação
""")
col_b1, col_b2 = st.columns(2)
with col_b1:
    st.image("../plots/corr.png")
with col_b2:
    st.markdown("""
        Pela análise de correlação entre as variáveis perceve-se que a única variável com uma correlação expressiva com
        o valor da corrida é a distância (*distance_km* - correlação de +0,84).
        
        Todas as outras variáveis apresentam uma correlação muito pequena com a variável alvo (*fare_amount*).
        
        A segunda melhor
        correlação ocorre com a variável do número de passageiros (*passenger_count*) que será usada para fazer a regressão linear múltipla.
    """)