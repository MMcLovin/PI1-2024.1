import asyncio
import websockets
import random
import json

async def send_data(websocket, path):
    while True:
        data = {
            'temperature': random.uniform(20.0, 30.0),
            'humidity': random.uniform(30.0, 60.0)
        }
        await websocket.send(json.dumps(data))
        await asyncio.sleep(1)  # Enviar dados a cada 1 segundo

start_server = websockets.serve(send_data, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
