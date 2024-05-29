<p style="text-align: justify">
# PI1-2024.1
 Repositório para organização do software relacionado ao projeto da disciplina de Projeto Integrador 1 de 2024.1


## Backlog


Dentro do planejamento auxiliado por metodologias ágeis, o Product Backlog é um artefato fundamental, pois é uma lista priorizada de requisitos, funcionalidades e tarefas a serem executadas no projeto ou produto. Ele destaca a divisão de grandes tarefas que podem ser - em ordem decrescente de especificidade - temas, épicos, histórias de usuário e tasks ([Referencia]()). O nosso backlog foi elaborado com base nos requisitos elicitados pela técnica de brainstorm com os membros do subgrupo, da equipe geral, de software no dia tal e hora tal, portanto, foram identificados os épicos, detalhados na [tabela tal]() e historias de usuário, detalhadas na [tabela tal](), que foram agrupados na [tabela tal]() para fornecer uma melhor visualização do backlog. 


### Épicos


| Épico | ID | Histórias de Usuário associadas | Rastreabilidade |
| :---: | :-:| :------------------: | :--------------------: | 
| Monitorar dados do robô seguidor de linha | EP01 | US0x | RX |
| Analisar dados do robô seguidor de linha | EP02 | US0x | RX |


### Histórias de usuário


| Título | ID | História de Usuário |  Rastreabilidade |
| :----: | :-:| :-----------------: | :--------------: |
| enviar dados dos sensores     | US01 |  |  | RX |
| armazenar dados dos sensores     | US02 |  | US01 | RX |
| tratar dados dos sensores     | US03 |  | US01 | RX |
| gerar gráficos a partir dos dados dos sensores     | US04 |  | US01 | RX |
| gerar gráficos a partir dos dados dos sensores     | US05 |  | US01 | RX |
| Conectar A ESP32 na mesma rede do servidor | US06 |  | US01 | RX |
| Conectar o servidor na mesma rede da ESP32 | US07 |  | US01 | RX |


### Backlog Funcional


| ID Épico | Épico | Histórias de Usuário | ID História de Usuário | Rastreabilidade |
| :------: | :---: | :------------------: | :--------------------: | :-------------: |
| EP0X | X | Título  | USX | US01 | RF18 |


## Diagrama de Casos de uso


De acordo com ([Referencia]()) casos de uso são componentes fundamentais da linguagem de modelagem unificada (UML), que identificam atores envolvidos e nomeiam tipos de interação. Eles são complementados por descrições textuais ou modelos gráficos, como diagramas de sequência ou de estados. Um diagrama de casos de uso de alto nível documenta essas interações, representando todas as possíveis interações descritas nos requisitos do sistema. Atores, que podem ser pessoas ou outros sistemas, são representados por figuras 'palito', enquanto as interações são mostradas como elipses conectadas por linhas, com flechas opcionais indicando o início das interações. O nosso diagrama de caso de uso, na [figura x]() representa como ator primário o microcontrolador ESP286, que inicia a interação com o sistema por meio do envio de dados dos sensores, conexão via websocket e ajuste da velocidade das rodas do robô. Já o nosso ator secundário, é o servidor com o qual a esp286 é conectada, onde armazenaremos os dados e realizaremos os tratamentos dos dados.


![caso-de-uso](assets/PI1%20-%20Use%20Cases.drawio.svg)


## Requisitos


### Requisitos Funcionais


| Tipo | Descrição |
| :--: | --------- |
| **RF01** | O servidor deve ser capaz de armazenar os dados recebidos dos sensores em um banco de dados |
| **RF02** | Os dados recebidos devem ser tratados para permitir análises posteriores |
| **RF03** | A trajetória percorrida pelo robô deve ser gerada a partir dos dados dos sensores |


### Requisitos Não-Funcionais


| Tipo | Descrição |
| :--: | --------- |
| **RNF01** | O banco de dados usado deve ser o SQLite |
| **RNF02** | A biblioteca matplotlib deve ser usada para gerar os gráficos |
| **RNF03** | Os gráficos devem estar legíveis (devem usar a representação mais apropriada para cada tipo de dado e as cores devem ser de alto contraste) |
| **RNF04** | Python deve ser linguagem usada para receber e tratar os dados da ESP |
| **RNF05** | O intervalo de tempo entre o recebimento de dados deve ser curto (até 1 segundo) |
| **RNF06** | O protocolo de comunicação com a ESP deverá ser websocket |
| **RNF07** | Os dados recebidos devem ser precisos (menos de 30% de erro) |


## Referências
>
</p>