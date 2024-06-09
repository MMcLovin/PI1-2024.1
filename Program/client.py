import asyncio
import websockets
import json
import mysql.connector


uri = "ws://localhost:8765"

def criar_conexao(host, usuario, senha, banco):
    return mysql.connector.connect(host=host, user=usuario, password=senha, database=banco)


def fechar_conexao(con):
    return con.close()


def insere_usuario(con, indece, numPercurso, velEsquerda, velDireita , aceleracaoX, aceleracaoY, aceleracaoZ, consumoBat, giroscopioX, giroscopioY, giroscopioZ, RPM):
    cursor = con.cursor()
    sql = "INSERT INTO CARRINHO (indece, numPercurso, velEsquerda, velDireita , aceleracaoX, aceleracaoY, aceleracaoZ, consumoBat, giroscopioX, giroscopioY, giroscopioZ, RPM) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    valores = (indece, numPercurso, velEsquerda, velDireita , aceleracaoX, aceleracaoY, aceleracaoZ, consumoBat, giroscopioX, giroscopioY, giroscopioZ, RPM)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()

async def start():
    
    async with websockets.connect(uri) as websocket:
        await websocket.send("1")

        con = criar_conexao("localhost", "samuel", "010718", "projetopi1") 

        while True:
            data = await websocket.recv(),

            dtJson = json.loads(data[0])

            
            insere_usuario(con, dtJson['indece'], dtJson['numPercurso'], dtJson['velEsquerda'], dtJson['velDireita'], 
                           dtJson['aceleracaoX'], dtJson['aceleracaoY'], dtJson['aceleracaoZ'], dtJson['consumoBat'], dtJson['giroscopioX'],
                           dtJson['giroscopioY'], dtJson['giroscopioZ'], dtJson['RPM'])  # Desempacota os valores e passa para a função insere_usuario()
            

            print(f"Indice inserido no banco: {dtJson['indece']}")

        fechar_conexao(con)  # Deve ser fora do loop

asyncio.get_event_loop().run_until_complete(start())
