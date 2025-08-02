import csv
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker('pt_BR')

# Configurações
canais_marketing = [
    "Google Ads",
    "Facebook",
    "Instagram",
    "Email Marketing",
    "Influencers",
    "Youtube",
    "LinkedIn",
    "TikTok",
    "Twitter",
    "SEO"
]

class Campanha:
    def __init__(self, id, canal, inicio, fim, custo_total):
        self.id = id
        self.canal = canal
        self.inicio = inicio
        self.fim = fim
        self.custo_total = custo_total

    @staticmethod
    def gerar_campanhas(n=20):
        campanhas = []
        for i in range(1, n + 1):
            # Gera período de 15 a 90 dias
            inicio = fake.date_between(start_date='-1y', end_date='today')
            fim = inicio + timedelta(days=random.randint(15, 90))
            
            # Custo proporcional à duração
            custo_base = random.uniform(500, 10000)
            custo_total = round(custo_base * (fim - inicio).days / 30, 2)  # Custo mensalizado
            
            campanhas.append(Campanha(
                id=i,
                canal=random.choice(canais_marketing),
                inicio=inicio,
                fim=fim,
                custo_total=custo_total
            ))
        return campanhas

    @staticmethod
    def exportar_csv(campanhas, nome_arquivo='campanhas_marketing.csv'):
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'CANAL', 'INICIO', 'FIM', 'CUSTO_TOTAL'])
            for c in campanhas:
                writer.writerow([
                    c.id,
                    c.canal,
                    c.inicio.strftime('%d/%m/%Y'),
                    c.fim.strftime('%d/%m/%Y'),
                    c.custo_total
                ])

campanhas = Campanha.gerar_campanhas(100)
Campanha.exportar_csv(campanhas)