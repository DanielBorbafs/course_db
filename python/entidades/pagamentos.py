import csv
import random
import datetime
from faker import Faker

fake = Faker('pt_BR')

# Intervalo da data de pagamento
inicio = datetime.date(2024, 1, 1)
fim = datetime.date(2025, 4, 8)

class Pagamento:
    def __init__(self, id, pedido_id, forma_pagamento, valor_pago, data_pagamento, parcelado):
        self.id = id
        self.pedido_id = pedido_id
        self.forma_pagamento = forma_pagamento
        self.valor_pago = valor_pago
        self.data_pagamento = data_pagamento
        self.parcelado = parcelado

    @staticmethod
    def gera_pagamentos(n=10, start_id=1, pedido_id_inicial=101):
        pagamentos = []
        for i in range(n):
            id_pagamento = start_id + i
            pedido_id = pedido_id_inicial + i
            forma_pagamento = random.choice(['PIX', 'BOLETO', 'CARTAO'])
            valor_pago = round(random.uniform(50.0, 1000.0), 2)
            data_pagamento = fake.date_between(start_date=inicio, end_date=fim)
            parcelado = random.choice(['S', 'N'])

            pagamento = Pagamento(
                id=id_pagamento,
                pedido_id=pedido_id,
                forma_pagamento=forma_pagamento,
                valor_pago=valor_pago,
                data_pagamento=data_pagamento,
                parcelado=parcelado
            )

            pagamentos.append(pagamento)
        return pagamentos

    @staticmethod
    def salva_em_csv(pagamentos, nome_arquivo='pagamentos.csv'):
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow([
                'ID', 'PEDIDO_ID', 'FORMA_PAGAMENTO',
                'VALOR_PAGO', 'DATA_PAGAMENTO', 'PARCELADO'
            ])
            for pagamento in pagamentos:
                writer.writerow([
                    pagamento.id,
                    pagamento.pedido_id,
                    pagamento.forma_pagamento,
                    f"{pagamento.valor_pago:.2f}".replace('.', ','),  # PT-BR formato
                    pagamento.data_pagamento.strftime('%d/%m/%Y'),
                    pagamento.parcelado
                ])

# Gerar e salvar 50 pagamentos com pedido_id de 101 a 150
pagamentos = Pagamento.gera_pagamentos(n=50, start_id=1, pedido_id_inicial=101)
Pagamento.salva_em_csv(pagamentos)
