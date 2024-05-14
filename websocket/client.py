#!/usr/bin/env python

from websockets.sync.client import connect

def hello():
    # uri = "ws://192.168.4.1:81"  # Este é o IP padrão do ESP32 em modo AP
    with connect("ws://localhost:8765") as websocket:
        websocket.send("Hello world!")
        message = websocket.recv()
        print(f"Received: {message}")

hello()