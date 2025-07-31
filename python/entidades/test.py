from clientes import Cliente


clientes = Cliente.gera_clientes(100)
for c in clientes:
    print(vars(c))