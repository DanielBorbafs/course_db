import oracledb

conn = oracledb.connect(
    user="dba_ecom",
    password="157820",
    dsn="localhost:1521/XEPDB1",  # ou "host:porta/servico"
    mode=oracledb.DEFAULT_AUTH
)

print("Conectado com sucesso!")
conn.close()
