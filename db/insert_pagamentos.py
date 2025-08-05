import oracledb
import pandas as pd
from datetime import datetime

# Caminho do CSV gerado
csv_path = 'pagamentos.csv'

# Nome das colunas conforme o CSV
colunas = ['ID', 'PEDIDO_ID', 'FORMA_PAGAMENTO', 'VALOR_PAGO', 'DATA_PAGAMENTO', 'PARCELADO']

# Lendo o CSV com formatação correta para números e datas
df = pd.read_csv(
    csv_path,
    names=colunas,
    header=0,
    sep=',',
    converters={
        'VALOR_PAGO': lambda x: float(x.replace(',', '.')),
        'DATA_PAGAMENTO': lambda x: datetime.strptime(x, '%d/%m/%Y')
    }
)

# Convertendo colunas para tipos corretos
df['ID'] = pd.to_numeric(df['ID'], errors='coerce')
df['PEDIDO_ID'] = pd.to_numeric(df['PEDIDO_ID'], errors='coerce')

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

# Filtrando apenas linhas com IDs válidos
df_filtrado = df[df['PEDIDO_ID'].isin(pedidos_validos)]

# Convertendo para tuplas para inserção
data = [tuple(row) for row in df_filtrado.itertuples(index=False, name=None)]

# SQL para INSERT
sql = """
INSERT INTO PAGAMENTOS (
    ID, PEDIDO_ID, FORMA_PAGAMENTO, VALOR_PAGO, DATA_PAGAMENTO, PARCELADO
) VALUES (
    :1, :2, :3, :4, :5, :6
)
"""

# Executando o insert com batcherrors habilitado
cursor.executemany(sql, data, batcherrors=True)

# Verificando erros
errors = cursor.getbatcherrors()
if errors:
    for error in errors:
        print(f"Erro na linha {error.offset}: {error.message}")
else:
    print("Todos os pagamentos foram inseridos com sucesso!")

# Finalizando
conn.commit()
cursor.close()
conn.close()
