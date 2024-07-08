import servico_db as servico
import conexao as db

def main():

    con = db.criar_conexao("localhost", "samuel", "010718", "projetopi1")
    aceleracao = servico.buscar_aceleracao(con, 1)
    corrente = servico.buscar_corrente(con, 1)
    velocidade = servico.buscar_velocidade(con, 1)

    print (aceleracao)
    print (corrente)
    print (velocidade)



if __name__ == '__main__':
    main()

