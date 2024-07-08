CREATE DATABASE IF NOT exists projetopi1;

USE ProjetoPI1;


CREATE TABLE CARRINHO(
    indece BIGINT,
    numPercurso INT,
    tempo TIME,
    temperatura DECIMAL(5,3),
    velEsquerda DECIMAL(5,3),
    velDireita DECIMAL(5,3),
    aceleracaoX DECIMAL(5,3),
    aceleracaoY DECIMAL(5,3),
    aceleracaoZ DECIMAL(5,3),
    corrente DECIMAL(5,3),
    giroscopioX DECIMAL(5,3),
    giroscopioY DECIMAL(5,3),
    giroscopioZ DECIMAL(5,3)
);