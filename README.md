<p style="text-align: justify">

# PI1-2024.1
 Repositório para organização do software relacionado ao projeto da disciplina de Projeto Integrador 1 de 2024.1


## Backlog


Dentro do planejamento auxiliado por metodologias ágeis, o Product Backlog é um artefato fundamental, pois é uma lista mutável e priorizada de requisitos, funcionalidades e tarefas a serem executadas no projeto ou produto ([Referencia2]()). Ele destaca a divisão de grandes tarefas que podem ser - em ordem decrescente de especificidade - temas, épicos, histórias de usuário e tasks. O nosso backlog foi elaborado com base nos requisitos elicitados pela técnica de brainstorm com os membros do subgrupo, da equipe geral, de software no dia 20 de maio, portanto, foram identificados os épicos, detalhados na [tabela tal]() e historias de usuário, detalhadas na [tabela tal](), que foram agrupados na [tabela tal]() que tanto reúne as histórias de usuário associadas a cada épico quanto disponibiliza a rastreabilidade referente aos requisitos. 


### Épicos


| Épico | ID | 
| :---: | :-:|  
| Monitorar dados do robô seguidor de linha | EP01 | 
| Analisar dados do robô seguidor de linha | EP02 | 


### Histórias de usuário


| Título | ID | História de Usuário | Critério de aceitação | 
| :----: | :-:| :-----------------: | --------------------- |
| ler dados dos sensores | **US01** | Para monitorar o desempenho do robô, precisamos que o microcontrolador leia os dados dos sensores | O microcontrolador recebe dados em intervalos de tempo regulares |
| enviar dados dos sensores | **US02** | Para analisar o desempenho do robô, precisamos que o microcontrolador envie dados dos sensores para o servidor | O microcontrolador envia dados com sucesso em intervalos regulares |
| armazenar dados dos sensores  | **US03** | Como desenvolvedor, quero que o servidor armazene os dados dos sensores para análise posterior | Dados recebidos são armazenados corretamente no banco de dados |
| tratar dados dos sensores     | **US04** | Para garantir a qualidade dos dados, precisamos que os dados dos sensores sejam tratados antes de serem armazenados | Dados são processados e erros são minimizados (menos de 15% de erro) |
| gerar gráficos a partir dos dados dos sensores   | **US05** | Como analista, quero gerar gráficos dos dados dos sensores para visualizar o desempenho do robô | Gráficos são gerados e visualizados corretamente usando matplotlib |
| Conectar a ESP32 e o servidor em uma mesma rede | **US06** | Para permitir a comunicação entre dispositivos, precisamos conectar a ESP32 na mesma rede do servidor | É possível acompanhar os dados coletados pela ESP286 pelo servidor |


### Backlog Funcional


| ID Épico | Épico | Título da História de Usuário | ID História de Usuário | Rastreabilidade |
| :------: | :---: | :------------------: | :--------------------: | :-------------: |
| EP01 | Monitorar dados do robô seguidor de linha | ler dados dos sensores  | US01 | RF01 |
| EP02 | Analisar dados do robô seguidor de linha | enviar dados dos sensores   | US02 | RF01 |
| EP02 | Analisar dados do robô seguidor de linha | armazenar dados dos sensores | US03 | RF01 |
| EP02 | Analisar dados do robô seguidor de linha | tratar dados dos sensores | US04 | RF02 |
| EP02 | Analisar dados do robô seguidor de linha | gerar gráficos a partir dos dados dos sensores   | US05 | RF03 |
| EP02 | Analisar dados do robô seguidor de linha | Conectar a ESP32 e o servidor em uma mesma rede  | US06 | RF01 |


## Diagrama de Casos de uso

De acordo com ([Referencia1]()) casos de uso são componentes fundamentais da linguagem de modelagem unificada (UML), que identificam atores envolvidos e nomeiam tipos de interação. Eles são complementados por descrições textuais ou modelos gráficos, como diagramas de sequência ou de estados. Um diagrama de casos de uso de alto nível documenta essas interações, representando todas as possíveis interações descritas nos requisitos do sistema. Atores, que podem ser pessoas ou outros sistemas, são representados por figuras 'palito', enquanto as interações são mostradas como elipses conectadas por linhas, com flechas opcionais indicando o início das interações. O nosso diagrama de caso de uso, na [figura x]() representa como ator primário o microcontrolador ESP286, que inicia a interação com o sistema por meio das seguintes ações: envio de dados dos sensores, conexão via websocket à rede wifi e ajuste da velocidade das rodas do robô. Já o nosso ator secundário, é o servidor com o qual a esp286 é conectada, por onde realizaremos o armazenamento e tratamento dos dados.


![caso-de-uso](assets/PI1%20-%20Use%20Cases.drawio.svg)


## Requisitos


### Requisitos Funcionais


| Tipo | Descrição |
| :--: | --------- |
| **RF01** | O servidor deve ser capaz de armazenar os dados recebidos dos sensores em um banco de dados |
| **RF02** | O sistema deve tratar os dados recebidos para permitir análises posteriores |
| **RF03** | O sistema deve gerar a trajetória percorrida pelo robô a partir dos dados dos sensores |


### Requisitos Não-Funcionais


| Tipo | Descrição |
| :--: | --------- |
| **RNF01** | O banco de dados usado deve ser o MySQL |
| **RNF02** | A biblioteca matplotlib deve ser usada para gerar os gráficos |
| **RNF03** | Os gráficos devem estar legíveis (devem usar a representação mais apropriada para cada tipo de dado e as cores devem ser de alto contraste) |
| **RNF04** | Python deve ser linguagem usada para receber e tratar os dados da ESP |
| **RNF05** | O intervalo de tempo entre o recebimento de dados deve ser curto (até 1 segundo) |
| **RNF06** | O protocolo de comunicação com a ESP deverá ser websocket |
| **RNF07** | Os dados recebidos devem ser precisos (menos de 15% de erro) |

## Diagrama de Estado de Maquina

Uma maquina de estados é qualquer dispositivo com a capacidade de armazenaros status um objeto em um determinado momento, mudar seus status e gerar ações, seu objetivo é demonstrar
o comportamento de um elemento por meio de um conjunto de transições de estado.
A Figura abaixo descreve os estados do Carrinho em funcionamento bem como possíveis transições.

![Estado de Maquina](assets/DIAGRAMA%20DE%20ESTADOS%201.png)


## Referências
> 1. @book{book:{104431635},
   title =     {Software Engineering: A Practitioner's Approach},
   author =    {Roger Pressman, Bruce Maxim},
   publisher = {McGraw-Hill Education},
   isbn =      {9781260548006; 1260548007},
   year =      {2019},
   edition =   {9},
   url =       {https://www.amazon.com/ISE-SOFTWARE-ENGINEERING-PRACTITIONERS-APPROACH/dp/1260548007}}
> 2. @book{book:{104431635},
   title =     {	Análise de metodologias ágeis : conceitos, aplicações e relatos sobre XP e Scrum},
   author =    {Balle, Andrea Raymundo},
   publisher = {Trabalhos de Conclusão de Curso de Graduação, Universidade Federal do Rio Grande do Sul},
   year =      {2011},
   url =       {https://lume.ufrgs.br/handle/10183/31028}}
</p>
