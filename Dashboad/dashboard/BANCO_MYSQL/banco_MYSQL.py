import mysql.connector
from conexao import criar_conexao, fechar_conexao
import random

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

aleatoria = 12

def main():
    con = criar_conexao("localhost", "root", "34841984Full@", "ProjetoPI1")
    for i in range(aleatoria):
        valores = ale()  # Chama a função ale() e armazena os valores retornados
        insere_usuario(con, *valores)  # Desempacota os valores e passa para a função insere_usuario()
    fechar_conexao(con)  # Deve ser fora do loop

if __name__ == "__main__":
    main()
