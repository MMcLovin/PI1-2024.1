import mysql.connector

def criar_conexao(host, usuario, senha, banco):
    return mysql.connector.connect(host=host, user=usuario, password=senha, database=banco)

def insere_usuario(con, indece, numPercurso, velEsquerda, velDireita , aceleracaoX, aceleracaoY, aceleracaoZ, consumoBat, giroscopioX, giroscopioY, giroscopioZ, RPM):
    cursor = con.cursor()
    sql = "INSERT INTO CARRINHO (indece, numPercurso, velEsquerda, velDireita , aceleracaoX, aceleracaoY, aceleracaoZ, consumoBat, giroscopioX, giroscopioY, giroscopioZ, RPM) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    valores = (indece, numPercurso, velEsquerda, velDireita , aceleracaoX, aceleracaoY, aceleracaoZ, consumoBat, giroscopioX, giroscopioY, giroscopioZ, RPM)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()

def fetch_data(con, sql):
    cursor = con.cursor()
    cursor.execute(sql)
    resutados = cursor.fetchall()
    cursor.close()

    return resutados


def fechar_conexao(con):
    return con.close()