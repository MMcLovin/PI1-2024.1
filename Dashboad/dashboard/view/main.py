import streamlit
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

streamlit.set_page_config(page_title="Projeto PI1")


with streamlit.container():
    streamlit.subheader("Dados estatísticos do Carrinho")

with streamlit.container():

    # Dados de exemplo: consumo de energia da bateria
    consumo_energia = 450  # em watts
    capacidade_bateria = 1000  # em watts

    # Calculando a porcentagem de consumo de energia
    porcentagem_consumida = (consumo_energia / capacidade_bateria) * 100

    # Criando um DataFrame para facilitar a visualização
    data_consumo = pd.DataFrame({
        'Consumo de Energia': [consumo_energia],
        'Capacidade da Bateria': [capacidade_bateria]
    })

    # Criando o gráfico de barras
    streamlit.subheader('Gráfico de Consumo Energético')
    streamlit.bar_chart(data_consumo)

    # Mostrando a porcentagem de consumo de energia
    streamlit.write(f"Consumo de Energia: {consumo_energia} W")
    streamlit.write(f"Capacidade da Bateria: {capacidade_bateria} W")
    streamlit.write(f"Porcentagem de Consumo: {porcentagem_consumida:.2f}%")

with streamlit.container():
    # Criando dados de exemplo
    data = pd.DataFrame({
        'x': range(1, 11),
        'y': np.random.randint(1, 20, size=10)
    })
    # Criando um gráfico de linhas
    streamlit.subheader('Velocidade Instantãnea')
    fig, ax = plt.subplots()
    ax.plot(data['x'], data['y'])
    # Ajustando o tamanho da figura
    fig.set_size_inches(8, 4)  # Largura, Altura
    streamlit.pyplot(fig)

# streamlit run DashBoard/view/main.py
    
# Trajetória percorrida
# Velocidade instantânea
# Aceleração instantânea
# Tempo de percurso
# Consumo energético