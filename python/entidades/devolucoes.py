import csv
import random
import datetime
from faker import Faker

fake = Faker('pt_BR')

ids_com_devolucao = [
    5, 11, 20, 22, 24, 26, 28, 29, 36, 40, 45, 47, 59, 67,
    68, 69, 75, 77, 82, 87, 88, 90, 93, 94, 96, 99
]

inicio = datetime.date(2024, 1, 1)
fim = datetime.date(2025, 8, 1)

class Devolucao:
    def __init__(self, id, pedido_id, data_devolucao, motivo_devolucao):
        self.id = id  # ✔️ corrigido
        self.pedido_id = pedido_id
        self.data_devolucao = data_devolucao
        self.motivo_devolucao = motivo_devolucao

    @staticmethod
    def gera_devolucoes(ids_pedidos):
        motivos_devolucao = [
            'Produto com defeito',
            'Produto diferente do anunciado',
            'Tamanho incorreto',
            'Pedido duplicado',
            'Cliente desistiu da compra',
            'Produto chegou atrasado',
            'Produto danificado no transporte',
            'Erro na escolha do produto',
            'Embalagem violada',
            'Insatisfação com a qualidade'
        ]
        devolucoes = []
        for i, pedido_id in enumerate(ids_pedidos, start=1):
            data_devolucao = fake.date_between(start_date=inicio, end_date=fim)
            motivo_devolucao = random.choice(motivos_devolucao)

            devolucao = Devolucao(
                id=i,
                pedido_id=pedido_id,
                data_devolucao=data_devolucao,
                motivo_devolucao=motivo_devolucao
            )
            devolucoes.append(devolucao)
        return devolucoes

    @staticmethod
    def salva_em_csv(devolucoes, nome_arquivo='devolucoes.csv'):
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'PEDIDO_ID', 'DATA_DEVOLUCAO', 'MOTIVO_DEVOLUCAO'])
            for d in devolucoes:
                writer.writerow([
                    d.id,
                    d.pedido_id,
                    d.data_devolucao.strftime('%d/%m/%Y'),
                    d.motivo_devolucao
                ])

# ✔️ Use a lista de IDs de devoluções
devolucoes = Devolucao.gera_devolucoes(ids_com_devolucao)
Devolucao.salva_em_csv(devolucoes)
