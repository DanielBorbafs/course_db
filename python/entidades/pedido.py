import csv
from faker import Faker
import random 
import datetime


fake = Faker('pt_BR')

# Intervalo de datas personalizados para as vendas
inicio = datetime.date(2024,1,1)
fim = datetime.date(2025,4,8)

#

class Pedido:
    def __init__(self, id, cliente_id, vendedor_id, data_pedido, canal_venda, status_pedido):
        self.id = id 
        self.cliente_id = cliente_id
        self.vendedor_id = vendedor_id
        self.data_pedido = data_pedido
        self.canal_venda = canal_venda
        self.status_pedido = status_pedido
    @staticmethod
    def gera_pedidos(n=10, start_id= 1):
        pedidos = []
        for i in range(start_id, start_id + n):
            cliente_id = random.randint(1,99)
            vendedor_id = random.randint(1,99)
            data_pedido = fake.date_between(start_date = inicio, end_date =fim )
            canal_venda = random.choice(['Ecommerce', 'Loja física'])
            status_pedido = random.choice(['Finalizado'])

            pedido = Pedido(
                id = i,
                cliente_id=cliente_id,
                vendedor_id=vendedor_id,
                data_pedido=data_pedido,
                canal_venda=canal_venda,
                status_pedido=status_pedido
            )

            pedidos.append(pedido)
        return pedidos
    @staticmethod
    def salva_em_csv(pedidos, nome_arquivo= 'pedidos.csv'):
        with open(nome_arquivo, mode ='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)

            for pedido in pedidos:
                writer.writerow([
                    pedido.id,
                    pedido.cliente_id,
                    pedido.vendedor_id,
                    pedido.data_pedido.strftime('%d/%m/%Y'),
                    pedido.canal_venda,
                    pedido.status_pedido
                ])


pedidos = Pedido.gera_pedidos(n= 50, start_id = 101)
Pedido.salva_em_csv(pedidos)

