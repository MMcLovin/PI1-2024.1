CREATE DATABASE IF NOT exists projetopi1;

USE ProjetoPI1;


CREATE TABLE CARRINHO(
    indece BIGINT,
    numPercurso INT,
    tempo TIME,
    temperatura DECIMAL,
    velEsquerda DECIMAL,
    velDireita DECIMAL,
    aceleracaoX DECIMAL,
    aceleracaoY DECIMAL,
    aceleracaoZ DECIMAL,
    corrente DECIMAL,
    giroscopioX DECIMAL,
    giroscopioY DECIMAL,
    giroscopioZ DECIMAl
);