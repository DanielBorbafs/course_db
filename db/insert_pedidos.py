import oracledb
import pandas as pd

csv_path = 'pedidos.csv'


colunas = ['ID', 'CLIENTE_ID', 'VENDEDOR_ID', 'DATA_PEDIDO', 'CANAL_VENDA', 'STATUS_PEDIDO']

df = pd.read_csv(
    csv_path,
    names=colunas,
    header=0  
)

conn = oracledb.connect(
    user="dba_ecom",
    password="157820",
    dsn="localhost:1521/XEPDB1"
)

cursor = conn.cursor()

sql = """
INSERT INTO PEDIDOS (
    ID, CLIENTE_ID, VENDEDOR_ID, DATA_PEDIDO, CANAL_VENDA, STATUS_PEDIDO
) VALUES (
    :1, :2, :3, :4, :5, :6
)
"""


data = [tuple(row) for row in df.itertuples(index=False)]


cursor.executemany(sql, data)


conn.commit()
cursor.close()
conn.close()

print('Dados inseridos com sucesso na tabela PEDIDOS!')
