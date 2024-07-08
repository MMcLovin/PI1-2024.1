import asyncio
from time import sleep
import websockets
import json
import conexao
import datetime

uri = "ws://localhost:8765"
#uri = "ws://192.168.4.1:81"

numPercurso = 0

async def start():
    
    global numPercurso

    async with websockets.connect(uri) as websocket:
        
        await websocket.send("1")

        con = conexao.criar_conexao("localhost", "samuel", "010718", "projetopi1") 

        indece = 1

        while True:
            data = await websocket.recv(),

            # deve ser aqui porque converter dados demora um tempo consideravel
            tempo = datetime.datetime.now().time()
            
            
            dtJson = json.loads(data[0])

            #print(dtJson)

            # implementar alguma forma de para de gravar os dados
            # if
            # break
            
            conexao.insere_dados(
                con, 
                indece, 
                tempo, 
                numPercurso, 
                round(dtJson['temperatura'],3) ,
                round(dtJson['velEsquerda'],3),  
                round(dtJson['velDireita'],3),
                round(dtJson['aceleracaoX'],3),
                round(dtJson['aceleracaoY'],3),
                round(dtJson['aceleracaoZ'],3),
                round(dtJson['corrente'],3),
                round(dtJson['giroscopioX'],3),
                round(dtJson['giroscopioY'],3),
                round(dtJson['giroscopioZ'],3)
                      
            ) 
            
            indece += 1

            #sleep(0.1)

        conexao.fechar_conexao(con)  # Deve ser fora do loop


if __name__ == '__main__':

    print("Informe o número do percurso: ")
    numPercurso = int(input())


    asyncio.get_event_loop().run_until_complete(start())