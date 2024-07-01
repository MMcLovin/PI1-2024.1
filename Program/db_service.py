from decimal import Decimal
import conexao
import pandas as pd


# Responsável por criar consulta e retornar Dataframe

def get_aceleracao(con):
    consulta = "SELECT indece, numPercurso, aceleracaoX, aceleracaoY, aceleracaoZ FROM CARRINHO ORDER BY indece;"

    dados = conexao.fetch_data(con, consulta)
    lista_resultados = [[float(item) if isinstance(item, Decimal) else item for item in linha]
            for linha in dados
    ]

    df = pd.DataFrame(lista_resultados, columns=["indece", "numPercurso", "aceleracaoX", "aceleracaoY", "aceleracaoZ"])

    return df

def get_velocidade(con):
    consulta = "SELECT indece, numPercurso, velEsquerda, velDireita FROM CARRINHO ORDER BY indece;"

    dados = conexao.fetch_data(con, consulta)
    lista_resultados = [[float(item) if isinstance(item, Decimal) else item for item in linha]
            for linha in dados
    ]

    df = pd.DataFrame(lista_resultados, columns=["indece", "numPercurso", "velEsquerda", "velDireita"])

    return df
#def get_velocidade(con):
#def get_velocidade(con):
#def get_velocidade(con):
#def get_velocidade(con):

