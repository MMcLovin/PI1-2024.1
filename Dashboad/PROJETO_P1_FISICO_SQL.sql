CREATE DATABASE ProjetoPI1;
use ProjetoPI1;

CREATE TABLE CARRINHO(
	idCarrinho INT primary key not null,
    nome VARCHAR(30),
    velocidade DECIMAL(5,2),
    aceleracao DECIMAL(5,2),
    consumoBat DECIMAL(10,2)
) engine = InnoDB;