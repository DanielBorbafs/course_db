import oracledb
import pandas as pd

csv_path = 'cliques_campanhas.csv'


colunas = ["ID", "CLIENTE_ID", "CAMPANHA_ID", "DATA_CLIQUE", "PRODUTO_ID"]


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
INSERT INTO CLIQUES_CAMPANHA (
    ID, CLIENTE_ID, CAMPANHA_ID, DATA_CLIQUE, PRODUTO_ID
) VALUES (
    :1, :2, :3, :4, :5
)
"""


data = [tuple(row) for row in df.itertuples(index=False)]


cursor.executemany(sql, data)


conn.commit()
cursor.close()
conn.close()

print('Dados inseridos com sucesso na tabela CLIQUES CAMPANHAS!')
