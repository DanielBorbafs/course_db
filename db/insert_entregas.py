import oracledb
import pandas as pd

# Caminho para o arquivo CSV
csv_path = 'entregas.csv'

# Nome das colunas
colunas = ['ID', 'PEDIDO_ID', 'DATA_ENVIO', 'DATA_ENTREGA', 'TRANSPORTADORA', 'FRETE', 'STATUS_ENTREGA']

# Lendo o CSV
df = pd.read_csv(
    csv_path,
    names=colunas,
    header=0,
    dayfirst=True  # para interpretar datas no formato brasileiro (DD/MM/YYYY)
)

# 🔧 Conversão de tipos
df['ID'] = pd.to_numeric(df['ID'], errors='coerce')
df['PEDIDO_ID'] = pd.to_numeric(df['PEDIDO_ID'], errors='coerce')
df['FRETE'] = pd.to_numeric(df['FRETE'], errors='coerce')

df['DATA_ENVIO'] = pd.to_datetime(df['DATA_ENVIO'], dayfirst=True, errors='coerce')
df['DATA_ENTREGA'] = pd.to_datetime(df['DATA_ENTREGA'], dayfirst=True, errors='coerce')

# Convertendo para datetime.date (necessário para Oracle)
df['DATA_ENVIO'] = df['DATA_ENVIO'].dt.date
df['DATA_ENTREGA'] = df['DATA_ENTREGA'].dt.date

# Conectando ao Oracle
conn = oracledb.connect(
    user="dba_ecom",
    password="157820",
    dsn="localhost:1521/XEPDB1"
)

cursor = conn.cursor()

# 🔍 Buscando os PEDIDO_ID válidos no banco
cursor.execute("SELECT ID FROM PEDIDOS")
pedidos_validos = [row[0] for row in cursor.fetchall()]

# 🎯 Filtrando apenas entregas com PEDIDO_ID existentes
df_filtrado = df[df['PEDIDO_ID'].isin(pedidos_validos)]

# Montando os dados para inserção
data = [tuple(row) for row in df_filtrado.itertuples(index=False, name=None)]

# SQL de inserção
sql = """
INSERT INTO ENTREGAS (
    ID, PEDIDO_ID, DATA_ENVIO, DATA_ENTREGA, TRANSPORTADORA, FRETE, STATUS_ENTREGA
) VALUES (
    :1, :2, :3, :4, :5, :6, :7
)
"""

# Inserindo os dados com tratamento de erro em lote
cursor.executemany(sql, data, batcherrors=True)

# Mostrando erros (se houver)
errors = cursor.getbatcherrors()
if errors:
    for error in errors:
        print(f"Erro na linha {error.offset}: {error.message}")
else:
    print("Todos os dados foram inseridos com sucesso!")

# Finalizando
conn.commit()
cursor.close()
conn.close()
