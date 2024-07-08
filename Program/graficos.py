import streamlit
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import conexao as db
import servico_db as servico

streamlit.set_page_config(page_title="Projeto PI1")

# global variables
R=3.3625        # robot wheel radius
L=21.2          # distance between the robot wheels
n=20            # number of encoder ticks per wheel revolution


# Funções de plotagem
def gerar_grafico_velocidade(time, velE, velD):
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

def gerar_grafico_aceleracao(time, acc_abs):
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
def gerar_grafico_trajetoria(df):
    x_pos = [0]         # initial x position
    y_pos = [0]         # initial y position
    theta = 0           # initial heading

    for l, r in zip(df["velEsquerda"], df["velDireita"]):
        dr = r * ((2 * np.pi * R) / n)  # distance traveled by the right wheel
        dl = l * ((2 * np.pi * R) / n)  # distance traveled by the left wheel
        d = (dr + dl) / 2               # total distance traveled by the middle point between the wheels
        alfa = (dr - dl) / L           # change in heading
        theta += alfa                  # update heading
        x = d * np.cos(theta)          # distance traveled in x direction
        y = d * np.sin(theta)          # distance traveled in y direction
        x_pos.append(x_pos[-1] + x)    # update x position based on the last x position
        y_pos.append(y_pos[-1] + y)    # update y position based on the last y position
    plot_trajectory(x_pos, y_pos)


def gerar_grafico_corrente(time, numPercurso, corrente):
    fig, ax = plt.subplots(figsize=(10, 5))

    # Limpar o subplot antes de plotar novos dados
    ax.clear()

    ax.set_xlim(0, max(time))
    ax.set_ylim(min(corrente), max(corrente))

    # Plotar dados no subplot
    ax.plot(time, corrente, label='Acceleration X', color='blue', linestyle='solid', marker='o')
    # Configurar título, labels e outros elementos do subplot
    ax.set_title(f"Corrente ao longo do tempo")
    ax.set_xlabel('Tempo')
    ax.set_ylabel('Corrente')
    ax.legend()
    ax.grid(True)

    # Ajustar layout dos subplots
    plt.tight_layout()

    # Mostrar o gráfico na tela
    #plt.show()
    plt.savefig('corrente.png')  # Salvar o gráfico como um arquivo de imagem


def criarGrafico(conexao, numPercurso):

    # Buscar dados
    dfVelocidade = servico.buscar_velocidade(conexao, numPercurso)
    dfAceleracao = servico.buscar_aceleracao(conexao, numPercurso)
    dfCorrente = servico.buscar_corrente(conexao, numPercurso)

    dfVelocidade['velLinear'] = np.pi * R * (dfVelocidade['velEsquerda'] + dfVelocidade['velDireita']) / 60

    dfAceleracao['aceleracao_absoluta'] = (dfAceleracao['aceleracaoX']**2 + dfAceleracao['aceleracaoY']**2 + dfAceleracao['aceleracaoZ']**2)**0.5
    
    # DESCOBRIR FORMA DE AJUSTART OS GRAFICOS PARA NÃO FICAREM MUITO POLUIDOS
    dfVelocidade = dfVelocidade.iloc[:100]
    dfAceleracao = dfAceleracao.iloc[:100]
    dfCorrente = dfCorrente.iloc[:100]
    
    # ALTERAR PARA TEMPO DEPOIS DE VALIDA COM INDECE
    gerar_grafico_velocidade(dfVelocidade["indece"], dfVelocidade["velLinear"])
    gerar_grafico_aceleracao(dfAceleracao["indece"], dfAceleracao["aceleracao_absoluta"])
    gerar_grafico_corrente(dfCorrente["indece"], dfCorrente["numPercurso"], dfCorrente["corrente"])
    gerar_grafico_trajetoria(dfVelocidade)

def main():
    print("Escolha o numero do percurso para gerar gráficos (apenas o número):")
    
    numPercuros = int(input())

    con = db.criar_conexao("localhost", "user", "password", "projetopi1")

    criarGrafico(con, numPercuros)

    db.fechar_conexao(con)

if __name__ == '__main__':
    main()

