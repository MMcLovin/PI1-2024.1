import mysql.connector


def criar_conexao(host, usuario, senha, banco):
    return mysql.connector.connect(host=host, user=usuario, password=senha, database=banco)

def insere_dados(
        con, 
        indece, 
        tempo,
        numPercurso, 
        temperatura,
        velEsquerda, 
        velDireita, 
        aceleracaoX, 
        aceleracaoY, 
        aceleracaoZ, 
        corrente, 
        giroscopioX, 
        giroscopioY, 
        giroscopioZ):
    cursor = con.cursor()
    sql = "INSERT INTO CARRINHO (indece, tempo, numPercurso, temperatura, velEsquerda, velDireita , aceleracaoX, aceleracaoY, aceleracaoZ, corrente, giroscopioX, giroscopioY, giroscopioZ) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    valores = (indece, tempo, numPercurso, temperatura, velEsquerda, velDireita , aceleracaoX, aceleracaoY, aceleracaoZ, corrente, giroscopioX, giroscopioY, giroscopioZ)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()

def realizar_consulta(con, sql):
    cursor = con.cursor()
    cursor.execute(sql)
    resutados = cursor.fetchall()
    cursor.close()

    return resutados

def fechar_conexao(con):
    return con.close()
