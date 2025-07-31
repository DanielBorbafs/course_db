from faker import Faker
import random 
from datetime import date

fake = Faker('pt_BR')
genero = random.choice(['M', 'F'])


class Cliente:
    def __init__(self, id, nome, email, data_nascimento, sexo, uf, data_cadastro):
        self.id = id
        self.nome = nome
        self.email = email
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.uf = uf
        self.data_cadastro = data_cadastro
    @staticmethod
    def gera_clientes(n=10):
        clientes = []
        for i in range(1, n+1):
            sexo = random.choice(['M', 'F'])
            nome = fake.first_name_male() if sexo == 'M' else fake.first_name_female()
            sobrenome = fake.last_name()
            email = fake.email()
            data_nascimento = fake.date_of_birth(minimum_age=0, maximum_age=75)
            uf = fake.estado_sigla()
            data_cadastro = date.today()

            cliente = Cliente(
                id=i,
                nome=f"{nome} {sobrenome}",
                email=email,
                data_nascimento=data_nascimento,
                sexo=sexo,
                uf=uf,
                data_cadastro=data_cadastro
            )
            clientes.append(cliente)
        return clientes
    

