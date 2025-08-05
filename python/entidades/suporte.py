import csv
from faker import Faker
import random
import datetime

fake = Faker('pt_BR')

# Intervalo de datas para os tickets
inicio = datetime.date(2024, 1, 1)
fim = datetime.date(2025, 4, 8)

# Problemas típicos em ecommerce para o campo TIPO_PROBLEMA
problemas_ecommerce = [
    'Produto com defeito',
    'Atraso na entrega',
    'Pedido incorreto',
    'Problema no pagamento',
    'Produto indisponível',
    'Solicitação de troca',
    'Solicitação de devolução',
    'Dúvida sobre características do produto',
    'Cancelamento de pedido',
    'Cobrança indevida',
    'Problemas no site',
    'Suporte técnico necessário',
    'Reembolso não recebido',
    'Produto danificado na entrega',
    'Informações de rastreamento incorretas'
]

class TicketProblema:
    def __init__(self, id, cliente_id, pedido_id, data_ticket, tipo_problema, resolvido):
        self.id = id
        self.cliente_id = cliente_id
        self.pedido_id = pedido_id
        self.data_ticket = data_ticket
        self.tipo_problema = tipo_problema
        self.resolvido = resolvido

    @staticmethod
    def gera_tickets(n=10, start_id=1):
        tickets = []
        for i in range(start_id, start_id + n):
            cliente_id = random.randint(1, 99)
            pedido_id = random.randint(1, 149)  
            data_ticket = fake.date_between(start_date=inicio, end_date=fim)
            tipo_problema = random.choice(problemas_ecommerce)
            resolvido = random.choices(['S', 'N'], weights=[0.8, 0.2])[0]  

            ticket = TicketProblema(
                id=i,
                cliente_id=cliente_id,
                pedido_id=pedido_id,
                data_ticket=data_ticket,
                tipo_problema=tipo_problema,
                resolvido=resolvido
            )
            tickets.append(ticket)
        return tickets

    @staticmethod
    def salva_em_csv(tickets, nome_arquivo='tickets_problema.csv'):
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            
            writer.writerow(['ID', 'CLIENTE_ID', 'PEDIDO_ID', 'DATA_TICKET', 'TIPO_PROBLEMA', 'RESOLVIDO'])
            for ticket in tickets:
                writer.writerow([
                    ticket.id,
                    ticket.cliente_id,
                    ticket.pedido_id,
                    ticket.data_ticket.strftime('%d/%m/%Y'),
                    ticket.tipo_problema,
                    ticket.resolvido
                ])


if __name__ == "__main__":
    tickets = TicketProblema.gera_tickets(n=50, start_id=201)
    TicketProblema.salva_em_csv(tickets)
