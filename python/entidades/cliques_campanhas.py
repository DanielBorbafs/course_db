import csv
from faker import Faker
import random 
from datetime import date
import pandas as pd 

fake = Faker('pt_BR')

# Trazendo o numero de ids da campanha para fazer a relação
df_campanhas_range = pd.read_csv('campanhas_marketing.csv')
campanhas_range_id = df_campanhas_range.shape[0]
campanhas_range_id = int(campanhas_range_id)


# Trazendo o numero de ids dos clientes para fazer a relação
df_clientes_range = pd.read_csv('clientes.csv')
clientes_range_id = df_clientes_range.shape[0]
clientes_range_id = int(clientes_range_id)

# Trazendo o numero de ids dos produtos para fazer a relação
df_produtos_range = pd.read_csv('produtos.csv')
produtos_range_id = df_produtos_range.shape[0]
produtos_range_id = int(produtos_range_id)


class Cliques_Campanha:
    def  __init__ (self, id, cliente_id, campanha_id, data_clique, produto_id):
        self.id = id
        self.cliente_id = cliente_id
        self.campanha_id = campanha_id
        self.data_clique = data_clique
        self.produto_id = produto_id
    @staticmethod
    def gera_cliques(n = 10):
        cliques = []
        for i in range(1, n+1):
            cliente_id = random.randint(1, clientes_range_id)
            campanha_id = random.randint(1, campanhas_range_id)
            data_clique = fake.date_between(start_date='-1y', end_date='today').strftime('%d/%m/%Y')
            produto_id = random.randint(1, produtos_range_id)
            cliques.append(Cliques_Campanha(i, cliente_id, campanha_id, data_clique, produto_id))
        return cliques
    @staticmethod
    def exportar_csv(cliques, caminho_arquivo="cliques_campanhas.csv"):
        with open(caminho_arquivo, mode = 'w', newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "CLIENTE_ID", "CAMPANHA_ID", "DATA_CLIQUE", "PRODUTO_ID"])
            for c in cliques:
                writer.writerow([c.id, c.cliente_id, c.campanha_id, c.data_clique, c.produto_id])



cliques_gerados = Cliques_Campanha.gera_cliques(100)
Cliques_Campanha.exportar_csv(cliques_gerados)