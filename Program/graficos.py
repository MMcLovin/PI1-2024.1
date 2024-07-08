import streamlit
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import conexao
import Program.servico_db as db
import servico_db

streamlit.set_page_config(page_title="Projeto PI1")

# global variables
R=3.3625      # robot wheel radius
L=21.2        # distance between the robot wheels
n=20       # number of encoder ticks per wheel revolution

# global variables
# R=3.3625      # robot wheel radius
# L=21.2        # distance between the robot wheels
# n=20       # number of encoder ticks per wheel revolution


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

# Funções de plotagem
def plot_speed(time, velE, velD):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.clear()
    ax.set_xlim(0, max(time))
    ax.set_ylim(min(min(velE), min(velD)), max(max(velE), max(velD)))
    ax.plot(time, velE, label='Velocidade E', color='blue', linestyle='solid', marker='o')
    ax.plot(time, velD, label='Velocidade D', color='red', linestyle='solid', marker='o')
    ax.set_title("Velocidade ao longo do tempo")
    ax.set_xlabel('Tempo')
    ax.set_ylabel('Velocidade')
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    plt.savefig('velocidade.png')
    plt.show()
    plt.close(fig)

def plot_accelerations(time, acc_abs):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.clear()
    ax.set_xlim(0, max(time))
    ax.set_ylim(min(acc_abs), max(acc_abs))
    ax.plot(time, acc_abs, label='Aceleração Absoluta', color='blue', linestyle='solid', marker='o')
    ax.set_title(f"Aceleração Absoluta ao longo do tempo")
    ax.set_xlabel('Tempo')
    ax.set_ylabel('Aceleração Absoluta')
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    plt.savefig('aceleracao.png')
    plt.show()
    plt.close(fig)

def plot_trajectory(x_pos, y_pos):
    plt.plot(x_pos, y_pos, marker='o', color='b', label='Trajectory')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.title('Trajectory of Line Follower Robot')
    plt.grid(True)
    plt.savefig("trajetoria.png")
    plt.show()
    plt.close()

# Funções principais
def get_speed(con):
    df = get_velocidade(con)
    plot_speed(df["indece"], df["velEsquerda"], df["velDireita"])

def get_accelerations(con):
    df = get_aceleracao(con)
    df['aceleracao_absoluta'] = (df['aceleracaoX']**2 + df['aceleracaoY']**2 + df['aceleracaoZ']**2)**0.5
    plot_accelerations(df["indece"], df["aceleracao_absoluta"])

def generate_xy(con):
    x_pos = [0]
    y_pos = [0]
    theta = 0  # initial heading
    df = get_velocidade(con)
    for l, r in zip(df["velEsquerda"], df["velDireita"]):
        dr = r * ((2 * np.pi * 3.25) / 192)  # distance traveled by the right wheel
        dl = l * ((2 * np.pi * 3.25) / 192)  # distance traveled by the left wheel
        d = (dr + dl) / 2               # total distance traveled by the middle point between the wheels
        alfa = (dr - dl) / 16           # change in heading
        theta += alfa  # update heading
        x = d * np.cos(theta)
        y = d * np.sin(theta)
        x_pos.append(x_pos[-1] + x)
        y_pos.append(y_pos[-1] + y)
    plot_trajectory(x_pos, y_pos)

def criarGrafico(conexao, numGrafico):
    if numGrafico == 1:
        get_speed(conexao)
    elif numGrafico == 2:
        get_accelerations(conexao)
    elif numGrafico == 3:
        print("Consumo energético não implementado.")
    elif numGrafico == 4:
        generate_xy(conexao)

def main():
    print("Escolha o gráfico a ser gerado (apenas o número):")
    print("1 - Velocidade")
    print("2 - Aceleração")
    print("3 - Consumo energético")
    print("4 - Trajetória")
    numGrafico = int(input())
    con = criar_conexao("localhost", "root", "senha", "projetopi1")
    criarGrafico(con, numGrafico)
    fechar_conexao(con)

if __name__ == '__main__':
    main()

