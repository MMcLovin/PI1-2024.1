import mysql.connector
from conexao import criar_conexao, fechar_conexao
import random
import matplotlib.pyplot as plt

def insere_usuario(con, numPercurso, velEsquerda, velDireita , aceleracaoX, aceleracaoY, aceleracaoZ, consumoBat, tempoPercuso, giroscopioX, giroscopioY, giroscopioZ, RPM):
    cursor = con.cursor()
    sql = "INSERT INTO CARRINHO (numPercurso, velEsquerda, velDireita , aceleracaoX, aceleracaoY, aceleracaoZ, consumoBat, tempoPercuso, giroscopioX, giroscopioY, giroscopioZ, RPM) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    valores = (numPercurso, velEsquerda, velDireita , aceleracaoX, aceleracaoY, aceleracaoZ, consumoBat, tempoPercuso, giroscopioX, giroscopioY, giroscopioZ, RPM)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()

def ale():
    # Gerando uma tupla com 12 números de ponto flutuante aleatórios entre 0 e 1
    tupla = tuple(random.uniform(0, 1) for _ in range(12))
    return tupla

# o tempo tá como 0 usando ale(), mas ele deve ser um tempo condizente com o do percurso
def ale2(time):
    # Gerando uma tupla com 12 números de ponto flutuante aleatórios entre 0 e 1
    lista = []
    for i in range(12):
        if i != 7:
            lista.append(random.uniform(0, 1))
        else:
            lista.append(time)

    tupla = tuple(lista)

    return tupla

def fetch_data(con, sql):
    cursor = con.cursor()
    cursor.execute(sql)
    tuple_list = cursor.fetchall()
    cursor.close()

    return tuple_list

def create_list(con, tuple_list, data_list):
    for tuple in tuple_list:
        for value, robot_att in zip(tuple, data_list):            
            try:
                robot_att.append(value.total_seconds())
            except AttributeError:
                robot_att.append(float(value))
    
def print_velocities(con, v_left, v_right, time):
    print("V_left  V_right   Time")
    for i, j, k in zip(v_left, v_right, time):
        print(f"{i}     {j}     {k}")

def append_data(con, data, sql):
    tuple_list = fetch_data(con, sql)
    create_list(con, tuple_list, data)
    
def get_velocities(con):
    # nos dados reais, os valores já vão estar em ordem de tempo
    sql = "SELECT velEsquerda, velDireita, tempoPercuso, numPercurso FROM carrinho ORDER BY tempoPercuso;"

    v_left = []
    v_right = []
    time = []
    lap = []

    data = [v_left, v_right, time, lap]

    # o python passa os parametros por referência, então não precisa retornar a lista
    append_data(con, data, sql)

    plot_velocities(time, v_left, v_right)


def plot_velocities(time, v_left, v_right):
    plt.figure(figsize=(10, 5))
    plt.plot(time, v_left, label='Left Velocity', color='blue', linestyle='solid', marker='o')
    plt.plot(time, v_right, label='Right Velocity', color='red', linestyle='solid', marker='o')
    plt.title('Left and Right Velocities over Time')
    plt.xlabel('Time')
    plt.ylabel('Velocity')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():                               #SENHA  #BASE DE DADOS
    con = criar_conexao("localhost", "root", "", "ProjetoPI1") 

    # Quantidade de registros aleatórios a serem inseridos
    aleatoria = 20  
    time = 0
    #for i in range(aleatoria):
    #    valores = ale2(time)  # Chama a função ale() e armazena os valores retornados
    #    insere_usuario(con, *valores)  # Desempacota os valores e passa para a função 
    #    time += 1
    
    get_velocities(con)
    
    fechar_conexao(con)  # Deve ser fora do loop

if __name__ == "__main__":
    main()
