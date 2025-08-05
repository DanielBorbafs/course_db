import csv
from faker import Faker
import random 
import datetime


fake = Faker('pt_BR')

# Intervalo de datas personalizados para as vendas
inicio = datetime.date(2024,1,1)
fim = datetime.date(2025,4,8)

# Status entrega
status = ['Entregue', 'Em rota', 'Nao recebido']

class Entrega:
    def __init__ (self, id, pedido_id, data_envio, data_entrega, transportadora, frete, status_entrega):
        self.id = id 
        self.pedido_id = pedido_id
        self.data_envio = data_envio
        self.data_entrega = data_entrega
        self.transportadora = transportadora
        self.frete = frete
        self.status_entrega = status_entrega
    @staticmethod
    def gera_entregas(n=10, start_id=1):
        entregas = []
        for i in range(start_id, start_id + n):
            pedido_id = random.randint(1, 149)
            data_envio = fake.date_between(start_date=inicio, end_date=fim)

            status_entrega = random.choice(status)
            
            # Se entregue ou em rota, data de entrega posterior ao envio
            if status_entrega == 'Entregue':
                dias_para_entrega = random.randint(1, 10)
                data_entrega = data_envio + datetime.timedelta(days=dias_para_entrega)
            elif status_entrega == 'Em rota':
                data_entrega = None  # Ainda não foi entregue
            else:  # Não recebido
                data_entrega = None  # Pode deixar em branco também

            transportadora = fake.company()
            frete = round(random.uniform(15.0, 80.0), 2)

            entrega = Entrega(
                id=i,
                pedido_id=pedido_id,
                data_envio=data_envio,
                data_entrega=data_entrega,
                transportadora=transportadora,
                frete=frete,
                status_entrega=status_entrega
            )
            entregas.append(entrega)
        return entregas
    @staticmethod
    def salva_em_csv(entregas, nome_arquivo='entregas.csv'):
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)

            for entrega in entregas:
                writer.writerow([
                    entrega.id,
                    entrega.pedido_id,
                    entrega.data_envio.strftime('%d/%m/%Y'),
                    entrega.data_entrega.strftime('%d/%m/%Y') if entrega.data_entrega else '',
                    entrega.transportadora,
                    entrega.frete,
                    entrega.status_entrega
                 ])


entregas = Entrega.gera_entregas(145,2)
Entrega.salva_em_csv(entregas)