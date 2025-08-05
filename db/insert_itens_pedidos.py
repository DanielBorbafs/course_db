import oracledb
import pandas as pd

# Caminho do CSV gerado
csv_path = 'itens_pedido.csv'

# Nome das colunas conforme o CSV
colunas = ['ID', 'PEDIDO_ID', 'PRODUTO_ID', 'QUANTIDADE', 'PRECO_UNITARIO', 'DESCONTO']

# Lendo o CSV (substituindo ',' por '.' para números)
df = pd.read_csv(
    csv_path,
    names=colunas,
    header=0,
    sep=',',
    converters={
        'PRECO_UNITARIO': lambda x: float(x.replace(',', '.')),
        'DESCONTO': lambda x: float(x.replace(',', '.'))
    }
)

# Convertendo colunas para tipos corretos
df['ID'] = pd.to_numeric(df['ID'], errors='coerce')
df['PEDIDO_ID'] = pd.to_numeric(df['PEDIDO_ID'], errors='coerce')
df['PRODUTO_ID'] = pd.to_numeric(df['PRODUTO_ID'], errors='coerce')
df['QUANTIDADE'] = pd.to_numeric(df['QUANTIDADE'], errors='coerce')

# Conectando ao Oracle
conn = oracledb.connect(
    user="dba_ecom",
    password="157820",
    dsn="localhost:1521/XEPDB1"
)

cursor = conn.cursor()

# Verificando PEDIDO_IDs válidos
cursor.execute("SELECT ID FROM PEDIDOS")
pedidos_validos = {row[0] for row in cursor.fetchall()}

# Verificando PRODUTO_IDs válidos
cursor.execute("SELECT ID FROM PRODUTOS")
produtos_validos = {row[0] for row in cursor.fetchall()}

# Filtrando apenas linhas com IDs válidos
df_filtrado = df[
    df['PEDIDO_ID'].isin(pedidos_validos) &
    df['PRODUTO_ID'].isin(produtos_validos)
]

# Convertendo para tuplas para inserção
data = [tuple(row) for row in df_filtrado.itertuples(index=False, name=None)]

# SQL para INSERT
sql = """
INSERT INTO ITENS_PEDIDO (
    ID, PEDIDO_ID, PRODUTO_ID, QUANTIDADE, PRECO_UNITARIO, DESCONTO
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
    print("Todos os itens foram inseridos com sucesso!")

# Finalizando
conn.commit()
cursor.close()
conn.close()
