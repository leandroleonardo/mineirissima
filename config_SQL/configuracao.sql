CREATE DATABASE mineirissima;

USE mineirissima;

CREATE TABLE USUARIOS(
	id_usuario int not null primary key auto_increment,
	nome varchar(50) not null,
	senha varchar(20) not null,
	nivel int not null
);

CREATE TABLE PRODUTOS(
	id_produto int not null primary key auto_increment,
	nome varchar(100),
	ingredientes varchar(1000),
	grupo varchar(100),
	preco float
);

CREATE TABLE VENDAS(
	id_venda int not null primary key auto_increment,
	nome varchar(100) not null,
    id_usuario int,
    id_produto int,
    quantidade int,
    preco_total float,
    data_venda date,
	FOREIGN KEY (id_usuario) REFERENCES USUARIOS(id_usuario),
    FOREIGN KEY (id_produto) REFERENCES PRODUTOS(id_produto)
);

INSERT INTO USUARIOS(NOME, SENHA, NIVEL) VALUES ('admin','admin',2);

insert into produtos(nome, ingredientes, grupo, preco) values('Pão de queijo', 'Polvilho,  Leite, Óleo, Sal, Mussarela, Parmesão e Ovo', 'Pães', 1.5); #1
insert into produtos(nome, ingredientes, grupo, preco) values('Pão Recheado Pizza', 'Massa de Pão  Temperada,  Presunto, Mussarela,  Tomate e Orégano', 'Pães', 30); #2 
insert into produtos(nome, ingredientes, grupo, preco) values('Pão Recheado Três Queijos', 'Massa de Pão Temperada, Tomate, Mussarela,  Catupiry e Parmesão', 'Pães', 30); #2
insert into produtos(nome, ingredientes, grupo, preco) values('Pão Recheado Calabresa', 'Massa de Pão Temperada, Calabresa,  Mussarela, Cebola e Tomate', 'Pães', 30); #4
insert into produtos(nome, ingredientes, grupo, preco) values('Doce de Leite com Coco', 'Leite, Açucar,  Bicarbonato de Sódio,  Coco', 'Doces', 25); #5
insert into produtos(nome, ingredientes, grupo, preco) values('Doce de Leite com Ameixas', 'Leite, Açucar, Bicarbonato de Sódio,  Ameixa Desidratada', 'Doces', 25); #6
insert into produtos(nome, ingredientes, grupo, preco) values('Doce de Abóbora', 'Abóbora Madura, Açucar, Sal, Coco Fesco, Canela.', 'Doces', 20); #7