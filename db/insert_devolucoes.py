import oracledb
import pandas as pd

csv_path = 'devolucoes.csv'


colunas = ['ID', 'PEDIDO_ID', 'DATA_DEVOLUCAO', 'MOTIVO_DEVOLUCAO']

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
INSERT INTO DEVOLUCOES (
    ID, PEDIDO_ID, DATA_DEVOLUCAO, MOTIVO_DEVOLUCAO
) VALUES (
    :1, :2, :3, :4
)
"""


data = [tuple(row) for row in df.itertuples(index=False)]


cursor.executemany(sql, data)


conn.commit()
cursor.close()
conn.close()

print('Dados inseridos com sucesso na tabela DEVOLUCOES!')
