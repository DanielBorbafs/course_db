import oracledb
import pandas as pd
from datetime import datetime

# Caminho do CSV gerado com os tickets
csv_path = 'tickets_problema.csv'

# Nome das colunas conforme o CSV
colunas = ['ID', 'CLIENTE_ID', 'PEDIDO_ID', 'DATA_TICKET', 'TIPO_PROBLEMA', 'RESOLVIDO']

# Função para converter string da data no formato dd/mm/yyyy para datetime.date
def parse_data_ticket(data_str):
    try:
        return datetime.strptime(data_str, '%d/%m/%Y').date()
    except:
        return None

# Lendo o CSV
df = pd.read_csv(
    csv_path,
    names=colunas,
    header=0,
    sep=',',
    converters={
        'DATA_TICKET': parse_data_ticket,
        'ID': pd.to_numeric,
        'CLIENTE_ID': pd.to_numeric,
        'PEDIDO_ID': pd.to_numeric,
        'RESOLVIDO': str,
        'TIPO_PROBLEMA': str
    }
)

# Removendo linhas com data inválida
df = df.dropna(subset=['DATA_TICKET'])

# Conectando ao Oracle
conn = oracledb.connect(
    user="dba_ecom",
    password="157820",
    dsn="localhost:1521/XEPDB1"
)
cursor = conn.cursor()

# Opcional: buscar IDs válidos (exemplo, adapte ou comente se não quiser)
cursor.execute("SELECT ID FROM PEDIDOS")
pedidos_validos = {row[0] for row in cursor.fetchall()}

cursor.execute("SELECT ID FROM CLIENTES")
clientes_validos = {row[0] for row in cursor.fetchall()}

# Filtrando apenas linhas com PEDIDO_ID e CLIENTE_ID válidos
df_filtrado = df[
    df['PEDIDO_ID'].isin(pedidos_validos) &
    df['CLIENTE_ID'].isin(clientes_validos)
]

# Convertendo para tuplas para inserção
# OBS: DATA_TICKET como datetime.date é aceito pelo driver Oracle
data = [
    (
        row.ID,
        row.CLIENTE_ID,
        row.PEDIDO_ID,
        row.DATA_TICKET,
        row.TIPO_PROBLEMA,
        row.RESOLVIDO
    )
    for row in df_filtrado.itertuples(index=False)
]

# SQL para INSERT
sql = """
INSERT INTO SUPORTE (
    ID, CLIENTE_ID, PEDIDO_ID, DATA_TICKET, TIPO_PROBLEMA, RESOLVIDO
) VALUES (
    :1, :2, :3, :4, :5, :6
)
"""

# Executando o insert
cursor.executemany(sql, data, batcherrors=True)

# Verificando erros
errors = cursor.getbatcherrors()
if errors:
    for error in errors:
        print(f"Erro na linha {error.offset}: {error.message}")
else:
    print("Todos os tickets foram inseridos com sucesso!")

# Finalizando
conn.commit()
cursor.close()
conn.close()
