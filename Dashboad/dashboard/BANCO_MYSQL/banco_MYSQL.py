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

aleatoria = 12

def ale():
    # Gerando uma tupla com 12 números de ponto flutuante aleatórios entre 0 e 1
    tupla = tuple(random.uniform(0, 1) for _ in range(12))
    return tupla


def main():
    con = criar_conexao("localhost", "root", "34841984Full@", "ProjetoPI1")
    for i in range(aleatoria):
        k = ale
        insere_usuario(con, ale[1], ale[2], ale[3], ale[4], ale[5], ale[6], ale[7], ale[8], ale[9], ale[10])
        fechar_conexao(con)


if __name__ == "__main__":
    main()
