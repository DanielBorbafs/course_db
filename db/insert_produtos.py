import oracledb
import pandas as pd

csv_path = 'produtos.csv'


colunas = ['ID', 'NOME_PRODUTO', 'CATEGORIA', 'MARCA', 'PRECO', 'CUSTO', 'ESTOQUE_ATUAL']

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
INSERT INTO PRODUTOS (
    ID, NOME_PRODUTO, CATEGORIA, MARCA, PRECO, CUSTO, ESTOQUE_ATUAL
) VALUES (
    :1, :2, :3, :4, :5, :6, :7
)
"""


data = [tuple(row) for row in df.itertuples(index=False)]


cursor.executemany(sql, data)


conn.commit()
cursor.close()
conn.close()

print('Dados inseridos com sucesso na tabela PRODUTOS!')
