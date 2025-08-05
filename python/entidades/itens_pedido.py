import csv
import random
from faker import Faker

fake = Faker('pt_BR')

class ItemPedido:
    def __init__(self, id, pedido_id, produto_id, quantidade, preco_unitario, desconto):
        self.id = id
        self.pedido_id = pedido_id
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.desconto = desconto

    @staticmethod
    def gerar_itens(n=200, start_id=1):
        itens = []
        for i in range(start_id, start_id + n):
            pedido_id = random.randint(1, 150)           # IDs de pedidos existentes
            produto_id = random.randint(1, 100)            # IDs de produtos existentes
            quantidade = random.randint(1, 5)
            preco_unitario = round(random.uniform(20.0, 1000.0), 2)
            desconto = round(random.uniform(0.0, 30.0), 2)  # até 30 reais de desconto

            item = ItemPedido(
                id=i,
                pedido_id=pedido_id,
                produto_id=produto_id,
                quantidade=quantidade,
                preco_unitario=preco_unitario,
                desconto=desconto
            )
            itens.append(item)
        return itens

    @staticmethod
    def salvar_em_csv(itens, nome_arquivo='itens_pedido.csv'):
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            for item in itens:
                writer.writerow([
                    item.id,
                    item.pedido_id,
                    item.produto_id,
                    item.quantidade,
                    f'{item.preco_unitario:.2f}'.replace('.', ','),  # compatível com excel pt-BR
                    f'{item.desconto:.2f}'.replace('.', ',')
                ])

# 🔧 Gerando os dados
itens = ItemPedido.gerar_itens(n=500, start_id=1)
ItemPedido.salvar_em_csv(itens)
