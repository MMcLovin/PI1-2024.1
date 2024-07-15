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
INTERVALO_TEMPO = 0.1 # segundos


# Funções de plotagem
def gerar_grafico_velocidade(time, velocidade):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.clear()
    ax.set_xlim(0, max(time))
    ax.set_ylim(velocidade.min(), velocidade.max())
    ax.plot(time, velocidade, label='Velocidade E', color='blue', linestyle='solid', marker='o')
    # ax.plot(time, velD, label='Velocidade D', color='red', linestyle='solid', marker='o')
    ax.set_title("Velocidade ao longo do tempo")
    ax.set_xlabel('Tempo (s)')  # unidade de medida do eixo x
    ax.set_ylabel('Velocidade (m/s)')  # unidade de medida do eixo y
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
    ax.set_title("Aceleração Absoluta ao longo do tempo")
    ax.set_xlabel('Tempo (s)')  # unidade de medida no eixo x
    ax.set_ylabel('Aceleração Absoluta (m/s²)')  # Adiciona a unidade de medida no eixo y
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    plt.savefig('aceleracao.png')
    plt.show()
    plt.close(fig)

def plot_trajectory(x_pos, y_pos):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.clear()

    ax.plot(x_pos, y_pos, label='Trajetória', color='blue', linestyle='solid', marker='o')
    ax.set_title('Trajetória')
    ax.set_xlabel('Posição X (cm)')  # unidade de medida a do eixo x (estão em metros (m))
    ax.set_ylabel('Posição Y (cm)')  # unidade de medida  do eixo y (estão em metros (m))
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    plt.savefig('trajetoria.png')
    plt.close(fig)



    # plt.plot(x_pos, y_pos, marker='o', color='b', label='Trajectory')
    # plt.xlabel('X Position')
    # plt.ylabel('Y Position')
    # plt.title('Trajectory of Line Follower Robot')
    # plt.grid(True)
    # plt.savefig("trajetoria.png")
    # plt.show()
    # plt.close()

# Funções principais
def gerar_grafico_trajetoria(df):
    x_pos = [0]         # initial x position
    y_pos = [0]         # initial y position
    theta = 0           # initial heading

    for l, r in zip(df["velEsquerda"], df["velDireita"]):
        # Converter RPM para rad/s 
        w_l = (l * 2 * np.pi)/60
        w_r = (r * 2 * np.pi)/60

        # Calculo velocidade linear por meio de velocidade angular
        vel_linear_l = w_l * R
        vel_linear_r = w_r * R

        # Calculo da distância usando (MRU)
        dl = INTERVALO_TEMPO * vel_linear_l
        dr = INTERVALO_TEMPO * vel_linear_r

        # alternativa independente do tempo (rot/s * perimetro da roda)
        # dl = (l / 60) * 2 * np.pi * R 
        # dr = (l / 60) * 2 * np.pi * R 

        # distancia percorrida pelo ponto intermediario entre as rodas
        d = (dr + dl) / 2              

        # variação da orientação do robo 
        alfa = (dr - dl) / L           
        
        # distancia percorrida nos eixos x e y
        x = d * np.cos(theta)          
        y = d * np.sin(theta)          
        
        # atualiza posição nos eixos x e y, com base nas ultimas posições
        x_pos.append(x_pos[-1] + abs(x))    
        y_pos.append(y_pos[-1] + abs(y))    
        print(dl, dr, theta, x, y)

        # aualiza o angulo da nova orientação
        theta += alfa                  
    plot_trajectory(x_pos, y_pos)


def gerar_grafico_corrente(time, numPercurso, corrente):
    fig, ax = plt.subplots(figsize=(10, 5))

    # Limpar o subplot antes de plotar novos dados
    ax.clear()

    ax.set_xlim(0, max(time))
    ax.set_ylim(min(corrente), max(corrente))

    # Plotar dados no subplot
    ax.plot(time, corrente, label='Corrente', color='blue', linestyle='solid', marker='o')
    
    # Configurar título, labels e outros elementos do subplot
    ax.set_title("Corrente ao longo do tempo")
    ax.set_xlabel('Tempo (s)')  # unidade de medida  do eixo x
    ax.set_ylabel('Corrente (mA)')  # unidade de medida do eixo y
    ax.legend()
    ax.grid(True)

    # Ajustar layout dos subplots
    plt.tight_layout()

    # Mostrar o gráfico na tela
    # plt.show()
    plt.savefig('corrente.png')  # Salvar o gráfico como um arquivo de imagem
    plt.close(fig)  # Fecha a figura para liberar memória


def criarGrafico(conexao, numPercurso):

    # Buscar dados
    dfVelocidade = servico.buscar_velocidade(conexao, numPercurso)
    dfAceleracao = servico.buscar_aceleracao(conexao, numPercurso)
    dfCorrente = servico.buscar_corrente(conexao, numPercurso)

    dfVelocidade['velLinear'] = np.pi * R * (dfVelocidade['velEsquerda'] + dfVelocidade['velDireita']) / 60

    dfAceleracao['aceleracao_absoluta'] = (dfAceleracao['aceleracaoX']**2 + dfAceleracao['aceleracaoY']**2 + dfAceleracao['aceleracaoZ']**2)**0.5
    
    # DESCOBRIR FORMA DE AJUSTART OS GRAFICOS PARA NÃO FICAREM MUITO POLUIDOS
    # dfVelocidade = dfVelocidade.iloc[:100]
    # dfAceleracao = dfAceleracao.iloc[:100]
    # dfCorrente = dfCorrente.iloc[:100]
    
    # ALTERAR PARA TEMPO DEPOIS DE VALIDA COM INDECE
    gerar_grafico_velocidade(dfVelocidade["indece"], dfVelocidade["velLinear"])
    gerar_grafico_aceleracao(dfAceleracao["indece"], dfAceleracao["aceleracao_absoluta"])
    gerar_grafico_corrente(dfCorrente["indece"], dfCorrente["numPercurso"], dfCorrente["corrente"])
    gerar_grafico_trajetoria(dfVelocidade)

def main():
    print("Escolha o numero do percurso para gerar gráficos (apenas o número):")
    
    numPercuros = int(input())

    con = db.criar_conexao("localhost", "samuel", "010718", "projetopi1") 
    #con = db.criar_conexao("localhost", "root", "", "projetopi1")

    criarGrafico(con, numPercuros)

    db.fechar_conexao(con)

if __name__ == '__main__':
    main()

