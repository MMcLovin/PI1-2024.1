#include <ESP8266WiFi.h>
#include <WebSocketsServer.h>

// Pra rodar teve que baixar o https://arduino.esp8266.com/stable/package_esp8266com_index.json para conectar a esp na ide arduino
// baixar a biblioteca websockets by marcus sattler


// Colocar aqui as credenciais da internet
const char* ssid = "cerq a54";
const char* password = "laranjalima";

WebSocketsServer webSocket = WebSocketsServer(81); // Cria um websocket na porta 81

// Pin onde o led está conectada na esp8266 pin2
const int ledPin = 2; 

void setup() {
  // Inicializa o Monitor Serial
  Serial.begin(115200);

  // conecta no wifi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  // Inicializa o pino que vai acender
  pinMode(ledPin, OUTPUT);

  // Inicia o WebSocket server
  webSocket.begin();
  webSocket.onEvent(webSocketEvent);
}

void loop() {
  // WebSocket loop
  webSocket.loop();

  // Blink do led
  digitalWrite(ledPin, HIGH); 
  webSocket.broadcastTXT("LED is ON");
  delay(3000); 

  digitalWrite(ledPin, LOW);
  webSocket.broadcastTXT("LED is OFF");
  delay(3000); 
}

// WebSocket event handler
void webSocketEvent(uint8_t num, WStype_t type, uint8_t *payload, size_t length) {
  switch(type) {
    case WStype_DISCONNECTED:
      Serial.printf("[%u] Disconnected!\n", num);
      break;
    case WStype_CONNECTED: {
      IPAddress ip = webSocket.remoteIP(num);
      Serial.printf("[%u] Connection from %s\n", num, ip.toString().c_str());
    }
      break;
    case WStype_TEXT:
      Serial.printf("[%u] Received text: %s\n", num, payload);
      break;
    case WStype_BIN:
      Serial.printf("[%u] Received binary data\n", num);
      break;
    case WStype_ERROR:
      Serial.printf("[%u] Error occurred\n", num);
      break;
  }
}
