import asyncio
import websockets
import json
import conexao

uri = "ws://localhost:8765"

async def start():
    
    async with websockets.connect(uri) as websocket:
        await websocket.send("1")

        con = conexao.criar_conexao("localhost", "samuel", "010718", "projetopi1") 

        while True:
            data = await websocket.recv(),

            dtJson = json.loads(data[0])

            
            conexao.insere_usuario(con, dtJson['indece'], dtJson['numPercurso'], dtJson['velEsquerda'], dtJson['velDireita'], 
                           dtJson['aceleracaoX'], dtJson['aceleracaoY'], dtJson['aceleracaoZ'], dtJson['consumoBat'], dtJson['giroscopioX'],
                           dtJson['giroscopioY'], dtJson['giroscopioZ'], dtJson['RPM'])  # Desempacota os valores e passa para a função insere_usuario()
            

            print(f"Indice inserido no banco: {dtJson['indece']}")

        conexao.fechar_conexao(con)  # Deve ser fora do loop

asyncio.get_event_loop().run_until_complete(start())
