import asyncio
import websockets
import random
import json


# Função que simula os dados recebidos dos sensores
def dadoAleatorio():
    # Gerando uma tupla com 11 números de ponto flutuante aleatórios entre 0 e 1
    tupla = tuple(random.uniform(0, 1) for _ in range(11))
    return tupla

async def send_data(websocket, path):

    async for menssage in websocket:
        try:
            number = int(menssage)
            print("==== start ====")
            print(number)

            if number == 1:
                indece = 0
                volta = 1                
                dados = dadoAleatorio()
                while True:
                    data = {
                        'indece' : indece,
                        'numPercurso' : volta,
                        'velEsquerda' : dados[1],
                        'velDireita' : dados[2], 
                        'aceleracaoX' : dados[3],
                        'aceleracaoY' : dados[4],
                        'aceleracaoZ' : dados[5],
                        'consumoBat' : dados[6],
                        'giroscopioX' : dados[7],
                        'giroscopioY' : dados[8],
                        'giroscopioZ' : dados[9],
                        'RPM' : dados[10]
                        
                    }
                    await websocket.send(json.dumps(data))
                    await asyncio.sleep(1)  # Enviar dados a cada 1 segundo
                    indece += 1

        except ValueError:
            # Caso a mensagem não seja um número, envia uma mensagem de erro
            error_message = "Invalid input, please send a number."
            await websocket.send(error_message)
            print(f"Sent error message: {error_message}")


start_server = websockets.serve(send_data, "localhost", 8765)


asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
