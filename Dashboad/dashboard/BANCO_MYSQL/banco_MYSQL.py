import mysql.connector
from conexao import criar_conexao, fechar_conexao

def insere_usuario(con, idCarrinho, nome, velocidade, aceleracao, consumoBat):
    cursor = con.cursor()
    sql = "INSERT INTO CARRINHO (idCarrinho, nome, velocidade, aceleracao, consumoBat) values (%s, %s, %s, %s, %s)"
    valores = (idCarrinho, nome, velocidade, aceleracao, consumoBat)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()


def main():
    con = criar_conexao("localhost", "root", "34841984Full@", "ProjetoPI1")
    insere_usuario(con,'4', 'seguidor3', '12','200','40.5')
    fechar_conexao(con)


if __name__ == "__main__":
    main()