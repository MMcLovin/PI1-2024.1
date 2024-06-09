import mysql.connector
from conexao import criar_conexao, fechar_conexao
import random

def insere_usuario(con, indece, numPercurso, velEsquerda, velDireita , aceleracaoX, aceleracaoY, aceleracaoZ, consumoBat, giroscopioX, giroscopioY, giroscopioZ, RPM):
    cursor = con.cursor()
    sql = "INSERT INTO CARRINHO (indece, numPercurso, velEsquerda, velDireita , aceleracaoX, aceleracaoY, aceleracaoZ, consumoBat, giroscopioX, giroscopioY, giroscopioZ, RPM) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    valores = (indece, numPercurso, velEsquerda, velDireita , aceleracaoX, aceleracaoY, aceleracaoZ, consumoBat, giroscopioX, giroscopioY, giroscopioZ, RPM)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()

def ale():
    # Gerando uma tupla com 11 números de ponto flutuante aleatórios entre 0 e 1
    tupla = tuple(random.uniform(0, 1) for _ in range(11))
    return tupla

aleatoria = 12

def main():                                     #SENHA        #BASE DE DADOS
    con = criar_conexao("localhost", "samuel", "010718", "projetopi1") 
    for i in range(aleatoria):
        valores = ale()  # Chama a função ale() e armazena os valores retornados
        

        insere_usuario(con, i, *valores)  # Desempacota os valores e passa para a função insere_usuario()
    fechar_conexao(con)  # Deve ser fora do loop

if __name__ == "__main__":
    main()
