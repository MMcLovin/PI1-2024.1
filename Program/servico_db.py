from decimal import Decimal
import conexao
import pandas as pd


# Responsável por criar consulta e retornar Dataframe

def buscar_aceleracao(con, numPercurso):
    consulta = f"SELECT indece, numPercurso, aceleracaoX, aceleracaoY, aceleracaoZ FROM CARRINHO WHERE numPercurso = {numPercurso} ORDER BY indece;"

    dados = conexao.realizar_consulta(con, consulta)
    lista_resultados = [[float(item) if isinstance(item, Decimal) else item for item in linha]
            for linha in dados
    ]

    df = pd.DataFrame(lista_resultados, columns=["indece", "numPercurso", "aceleracaoX", "aceleracaoY", "aceleracaoZ"])

    return df

def buscar_velocidade(con, numPercurso):
    consulta = f"SELECT indece, numPercurso, velEsquerda, velDireita FROM CARRINHO WHERE numPercurso = {numPercurso} ORDER BY indece;"
    
    dados = conexao.realizar_consulta(con, consulta)
    lista_resultados = [[float(item) if isinstance(item, Decimal) else item for item in linha]
            for linha in dados
    ]

    df = pd.DataFrame(lista_resultados, columns=["indece", "numPercurso", "velEsquerda", "velDireita"])

    return df

def buscar_corrente(con, numPercurso):
    consulta = f"SELECT indece, numPercurso, corrente FROM CARRINHO WHERE numPercurso = {numPercurso} ORDER BY indece;"

    dados = conexao.realizar_consulta(con, consulta)
    lista_resultados = [[float(item) if isinstance(item, Decimal) else item for item in linha]
            for linha in dados
    ]

    df = pd.DataFrame(lista_resultados, columns=["indece", "numPercurso", "corrente"])

    return df

