from clientes import Cliente


clientes = Cliente.gera_clientes(10)

Cliente.salva_em_csv(clientes)
