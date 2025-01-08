CREATE DATABASE EMPRESA;

USE EMPRESA;

create table Funcionarios (
	matricula INT PRIMARY KEY,
	nome VARCHAR(50),
	departamento VARCHAR(50),
	sexo CHAR(1),
	salario DECIMAL,
	formado BOOLEAN
);

