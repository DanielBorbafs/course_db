import oracledb
import pandas as pd 

# Caminho do CSV
csv_path = 'clientes.csv'

# Nomes das colunas
colunas = ['ID', 'NOME', 'EMAIL', 'DATA_NASCIMENTO', 'SEXO', 'UF', 'DATA_CADASTRO']

# Leitura do CSV com parsing de datas
df = pd.read_csv(
    csv_path,
    names=colunas,
    header=None,
    parse_dates=['DATA_NASCIMENTO', 'DATA_CADASTRO'],
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
INSERT INTO CLIENTES(
    ID, NOME, EMAIL, DATA_NASCIMENTO, SEXO, UF, DATA_CADASTRO
) VALUES (
    :1, :2, :3, :4, :5, :6, :7
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
