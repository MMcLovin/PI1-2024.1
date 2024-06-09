CREATE DATABASE IF NOT exists projetopi1;
use ProjetoPI1;


CREATE TABLE CARRINHO(
    indece BIGINT,
    numPercurso INT,
    velEsquerda DECIMAL(5,2),
    velDireita DECIMAL(5,2),
    aceleracaoX DECIMAL(5,3),
    aceleracaoY DECIMAL(5,3),
    aceleracaoZ DECIMAL(5,3),
    consumoBat DECIMAL(10,2),
    giroscopioX DECIMAL(5,3),
    giroscopioY DECIMAL(5,3),
    giroscopioZ DECIMAL(5,3),
    RPM INT
);
