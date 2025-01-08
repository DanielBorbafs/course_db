CREATE DATABASE EMPRESA;

USE EMPRESA;

drop table funcionarios;

create table Funcionarios (
	matricula INT PRIMARY KEY NOT NULL,
	nome VARCHAR(50),
	departamento VARCHAR(50),
	sexo CHAR(1),
	salario DECIMAL(10,2),
	formado BOOLEAN
);

INSERT INTO Funcionarios (matricula, nome, departamento, sexo, salario, formado) 
VALUES (6894, 'Sarah', 'Product Management', 'F', 6268.41, 0);

INSERT INTO Funcionarios (matricula, nome, departamento, sexo, salario, formado) 
VALUES (637, 'Joshuah', 'Training', 'M', 8067.13, 1);

-- Inserções corrigidas
insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) 
values (73, 'Graig', 'Accounting', 'M', 14014.39, true);

insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) 
values (16, 'Glyn', 'Research and Development', 'M', 5835.20, true);

insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) 
values (2049, 'Ruddie', 'Sales', 'M', 11791.46, true);

insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) 
values (8699, 'Julie', 'Sales', 'M', 6075.25, false);

insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) 
values (1, 'Charlie', 'Engineering', 'M', 8092.78, true);

insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) values (908, 'Leroy', 'Engineering', 'M', 14987.52, true);
insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) values (1023, 'Sydnie', 'Marketing', 'F', 11329.87, false);
insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) values (3210, 'Alastair', 'Legal', 'M', 9993.22, true);
insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) values (411, 'Kimberly', 'Research and Development', 'F', 7325.10, true);
insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) values (876, 'Geoff', 'Human Resources', 'M', 14403.45, false);
insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) values (1200, 'Darlene', 'Support', 'F', 13887.00, true);
insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) values (5478, 'Terrence', 'Sales', 'M', 5123.76, false);
insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) values (1349, 'Elsie', 'Business Development', 'F', 10345.61, true);

insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) values (2001, 'Alexis', 'Marketing', 'F', 8256.34, true);
insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) values (2002, 'Daniel', 'Engineering', 'M', 14523.12, true);
insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) values (2003, 'Nina', 'Sales', 'F', 11056.89, false);
insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) values (2004, 'Victor', 'Support', 'M', 9384.45, true);
insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) values (2005, 'Jenna', 'Human Resources', 'F', 10429.72, false);
insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) values (2006, 'Philip', 'Research and Development', 'M', 15112.50, true);
insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) values (2007, 'Cynthia', 'Business Development', 'F', 10976.34, false);
insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) values (2008, 'Jonathan', 'Legal', 'M', 11563.42, true);
insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) values (2009, 'Carla', 'Marketing', 'F', 9234.29, false);
insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) values (2010, 'Max', 'Engineering', 'M', 13784.55, true);
insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) values (2011, 'Olivia', 'Sales', 'F', 11528.63, false);
insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) values (2012, 'Ian', 'Support', 'M', 7894.38, true);
insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) values (2013, 'Susan', 'Human Resources', 'F', 11503.74, true);
insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) values (2014, 'Luis', 'Research and Development', 'M', 12657.80, false);
insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) values (2015, 'Patricia', 'Business Development', 'F', 9887.91, true);
insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) values (2016, 'Ethan', 'Legal', 'M', 11840.27, true);
insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) values (2017, 'Chloe', 'Marketing', 'F', 9325.41, false);
insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) values (2018, 'George', 'Engineering', 'M', 12364.22, true);
insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) values (2019, 'Sophia', 'Sales', 'F', 10574.19, true);
insert into Funcionarios (matricula, nome, departamento, sexo, salario, formado) values (2020, 'Elliot', 'Support', 'M', 10234.88, false);

select * from funcionarios;