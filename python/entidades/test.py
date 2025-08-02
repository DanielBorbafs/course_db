from produtos import Produto

produtos_gerados = Produto.gera_produtos(10)
Produto.exportar_csv(produtos_gerados, "produtos.csv")