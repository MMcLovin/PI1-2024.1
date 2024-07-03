import streamlit
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import conexao
from decimal import Decimal
import db_service as db
from db_service import get_aceleracao

streamlit.set_page_config(page_title="Projeto PI1")

# global variables
R=3.25      # wheel radius
L=16        # distance between the wheels
n=192       # number of encoder ticks per wheel revolution



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

# VELOCIDADE
def get_speed(con):

    df = db.get_velocidade(con)
    
    plot_speed(df["indece"], df["velEsquerda"], df["velDireita"])

def plot_speed(time, velE, velD):
    fig, ax = plt.subplots(figsize=(10, 5))

    # Limpar o subplot antes de plotar novos dados
    ax.clear()

    ax.set_xlim(0, max(time))
    ax.set_ylim(min(min(velE), min(velD)), max(max(velE), max(velD)))

    # Plotar dados no subplot
    ax.plot(time, velE, label='Velocidade E', color='blue', linestyle='solid', marker='o')
    ax.plot(time, velD, label='Velocidade D', color='red', linestyle='solid', marker='o')
    
    # Configurar título, labels e outros elementos do subplot
    ax.set_title("Velocidade ao longo do tempo")
    ax.set_xlabel('Tempo')
    ax.set_ylabel('Velocidade')
    ax.legend()
    ax.grid(True)

    # Ajustar layout dos subplots
    plt.tight_layout()

    # Mostrar o gráfico na tela
    #plt.show()
    plt.savefig('velocidade.png')  # Salvar o gráfico como um arquivo de imagem


# ACELERAÇÃO
def get_accelerations(con):
    # Nos dados reais, os valores já vão estar em ordem de tempo
    df = get_aceleracao(con)

    # Calcular a aceleração absoluta
    df['aceleracao_absoluta'] = (df['aceleracaoX']**2 + df['aceleracaoY']**2 + df['aceleracaoZ']**2)**0.5 # --> toda a equação está dentro da raiz 
    
    plot_accelerations(df["indece"], df["aceleracao_absoluta"], df["numPercurso"])
    
def plot_accelerations(time, acc_abs, lap):
    # Criar uma nova figura
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.set_xlim(0, max(time))
    ax.set_ylim(min(acc_abs), max(acc_abs))

    # Plotar dados no subplot
    ax.plot(time, acc_abs, label='Aceleração Absoluta', color='blue', linestyle='solid', marker='o')

    # Configurar título, labels e outros elementos do subplot
    ax.set_title(f"Aceleração Absoluta ao longo do tempo")
    ax.set_xlabel('Tempo')
    ax.set_ylabel('Aceleração Absoluta')
    ax.legend()
    ax.grid(True)

    # Ajustar layout dos subplots
    plt.tight_layout()

    # Mostrar o gráfico na tela
    plt.show()

    # Fechar a figura para liberar memória
    plt.close(fig)
    
# TREJETORIA
def generate_xy(con):
    x_pos = [0]
    y_pos = [0]
    theta = 0  # initial heading
    
    df = db.get_velocidade(con)
    
    for l, r in zip(df["velEsquerda"], df["velDireita"]):
        dr = r * ((2 * np.pi * R) / n)  # distance traveled by the right wheel
        dl = l * ((2 * np.pi * R) / n)  # distance traveled by the left wheel
        d = (dr + dl) / 2               # total distance traveled by the middle point between the wheels
        alfa = (dr - dl) / L            # change in heading

        theta += alfa  # update heading
        x = d * np.cos(theta)
        y = d * np.sin(theta)

        # update the position relative to the last position
        x_pos.append(x_pos[-1] + x)
        y_pos.append(y_pos[-1] + y)

    plot_trajectory(x_pos, y_pos)

def plot_trajectory(x_pos, y_pos):
    plt.plot(x_pos, y_pos, marker='o', color='b', label='Trajectory')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.title('Trajectory of Line Follower Robot')
    plt.grid(True)
    plt.savefig("trajetoria.png")


def criarGrafico(conexao, numGrafico):
    match numGrafico:
        case 1:
            get_speed(conexao)
        case 2:
            get_accelerations(conexao)
        case 3:
            print(3)
        case 4:
            generate_xy(conexao)

def main():
    print("Escolha o gráfico a ser gerado (apenas o número):")
    print("1 - Velocidade")
    print("2 - Aceleração")
    print("3 - Consumo energético")
    print("4 - Trajetória")

    numGrafico = int(input())

    con = conexao.criar_conexao("localhost", "samuel", "010718", "projetopi1")

    criarGrafico(con, numGrafico)



if __name__ == '__main__':
    main()
