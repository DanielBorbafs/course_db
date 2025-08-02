import csv
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker('pt_BR')

# Configurações
categorias_fornecedores = [
    "Hardware", "Software", "Periféricos", "Acessórios", "Distribuidor"
]

regioes = ["Sudeste", "Sul", "Nordeste", "Centro-Oeste", "Norte"]

class Fornecedor:
    def __init__(self, id, nome, categoria_produto, data_contrato):
        self.id = id
        self.nome = nome
        self.categoria_produto = categoria_produto
        self.data_contrato = data_contrato

    @staticmethod
    def gerar_fornecedores(n=30):
        fornecedores = []
        for i in range(1, n + 1):
            # Nome de fornecedor realista (ex: "TechGames Distribuidora Ltda")
            nome = f"{fake.company()} {fake.random_element(['Distribuidora', 'Importados', 'Games', 'Tech'])}"
            
            # Categoria aleatória + região para tornar único
            categoria = f"{random.choice(categorias_fornecedores)} - {random.choice(regioes)}"
            
            # Data de contrato nos últimos 5 anos
            data_contrato = fake.date_between(start_date='-5y', end_date='today')
            
            fornecedores.append(Fornecedor(
                id=i,
                nome=nome[:20],  # Limita a 20 caracteres (VARCHAR2(20))
                categoria_produto=categoria[:20],  # Limita a 20 caracteres
                data_contrato=data_contrato
            ))
        return fornecedores

    @staticmethod
    def exportar_csv(fornecedores, nome_arquivo='fornecedores_gamer.csv'):
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'NOME', 'CATEGORIA_PRODUTO', 'DATA_CONTRATO'])
            for f in fornecedores:
                writer.writerow([
                    f.id,
                    f.nome,
                    f.categoria_produto,
                    f.data_contrato.strftime('%d/%m/%Y')  # Formato DD/MM/YYYY
                ])

# Uso
fornecedores = Fornecedor.gerar_fornecedores(100) 
Fornecedor.exportar_csv(fornecedores)            