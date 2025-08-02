import csv
from faker import Faker
import random 
from datetime import date

fake = Faker('pt_BR')

class Vendedor:
    def __init__(self, id, nome, uf, data_entrada):
        self.id = id
        self.nome = nome
        self.uf = uf
        self.data_entrada = data_entrada
    @staticmethod
    def gera_vendedores(n = 10):
        vendedores = []
        for i in range(1, n+1):
            nome = fake.first_name()
            uf = fake.estado_sigla()
            data_entrada = date.today()

            vendedor = Vendedor(
                id = i,
                nome = nome,
                uf=uf,
                data_entrada = data_entrada
            )
            vendedores.append(vendedor)
        return vendedores
    @staticmethod
    def salva_em_csv(vendedores, nome_arquivo = 'vendedores.csv'):
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)

            for vendedor in vendedores:
                writer.writerow([
                    vendedor.id,
                    vendedor.nome,
                    vendedor.uf,
                    vendedor.data_entrada.strftime('%d/%m/%Y')
                ])
    