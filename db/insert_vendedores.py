import oracledb
import pandas as pd 

# Caminho do CSV
csv_path = 'vendedores.csv'

# Nomes das colunas
colunas = ['ID', 'NOME_VENDEDOR', 'UF', 'DATA_ENTRADA']

# Leitura do CSV com parsing de datas
df = pd.read_csv(
    csv_path,
    names=colunas,
    header=None,
    parse_dates=['DATA_ENTRADA'],
    date_parser=lambda x: pd.to_datetime(x, format="%d/%m/%Y")  # ajuste se necessário
)

# Conexão Oracle
conn = oracledb.connect(
    user="dba_ecom",
    password="157820",
    dsn="localhost:1521/XEPDB1"
)

cursor = conn.cursor()

# Query de insert
sql = """
INSERT INTO VENDEDORES(
    ID, NOME_VENDEDOR, UF, DATA_ENTRADA
) VALUES (
    :1, :2, :3, :4
)
"""

# Transforma o DataFrame em lista de tuplas
data = [tuple(row) for row in df.itertuples(index=False)]

# Executa os inserts em lote
cursor.executemany(sql, data)

# Commit e cleanup
conn.commit()
cursor.close()
conn.close()

print('Dados inseridos com sucesso!')
