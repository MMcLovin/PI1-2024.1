import mysql.connector

# conectando ao banco de dados local
conexao = mysql.connector.connect(host='localhost', 
                                  database='cadastro', 
                                  user='root', 
                                  password='') 

if conexao.is_connected():
    print('Conectado ao banco de dados CARALEO!')
    # O cursor é um objeto usado para interagir com o banco de dados, permitindo executar comandos SQL como SELECT, INSERT e tals
    cursor = conexao.cursor()

while(True):
    command = input("Digite o comando SQL: ")
    if command == 'exit':
        break
    else:
        cursor.execute(command)
        data = cursor.fetchall()
        for row in data:
            print(row)
conexao.close()
cursor.close()