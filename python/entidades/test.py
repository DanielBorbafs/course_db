from vendedores import Vendedor

vendedores = Vendedor.gera_vendedores(5)

Vendedor.salva_em_csv(vendedores)