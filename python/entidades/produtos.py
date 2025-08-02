import csv
from faker import Faker
import random 
from datetime import date

fake = Faker('pt_BR')

categorias = [
    "Consoles",
    "Acessórios",
    "Jogos",
    "Controles",
    "Headsets",
    "Gift Cards",
    "PC Gamer",
    "Monitores Gamer",
    "Teclados Mecânicos",
    "Cadeiras Gamer"
]

marcas_por_categoria = {
    "Consoles": ["Sony", "Microsoft", "Nintendo"],
    "Acessórios": ["Razer", "Logitech", "Redragon", "HyperX", "Multilaser"],
    "Jogos": ["Sony", "Microsoft", "Nintendo", "Ubisoft", "EA"],
    "Controles": ["Sony", "Microsoft", "8BitDo", "Logitech"],
    "Headsets": ["HyperX", "Razer", "Corsair", "Logitech", "Redragon"],
    "Gift Cards": ["PlayStation", "Xbox", "Steam", "Nintendo eShop"],
    "PC Gamer": ["Dell", "Acer", "Asus", "Lenovo", "HP"],
    "Monitores Gamer": ["Samsung", "LG", "AOC", "Philips", "BenQ"],
    "Teclados Mecânicos": ["Razer", "Corsair", "Logitech", "Redragon", "SteelSeries"],
    "Cadeiras Gamer": ["DXRacer", "ThunderX3", "Husky", "Mymax", "Alpha Gamer"]
}


class Produto:
    def __init__(self, id, nome_produto, categoria, marca, preco, custo, estoque_atual):
        self.id = id
        self.nome_produto = nome_produto
        self.categoria = categoria
        self.marca = marca
        self.preco = preco
        self.custo = custo
        self.estoque_atual= estoque_atual
    @staticmethod
    def gera_produtos(n = 10):
        produtos = []
        for i in range(1, n+1):
            categoria = random.choice(categorias)
            marca = random.choice(marcas_por_categoria[categoria])
            base_nome = fake.word().capitalize()
            nome_produto = f"{marca} {base_nome}"
            preco = round(random.uniform(100, 5000), 2)
            custo = round(preco * random.uniform(0.5, 0.9), 2)
            estoque = random.randint(0, 100)
            produtos.append(Produto(i, nome_produto, categoria, marca, preco, custo, estoque))
        return produtos
    @staticmethod
    def exportar_csv(produtos, caminho_arquivo="produtos.csv"):
        with open(caminho_arquivo, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "NOME_PRODUTO", "CATEGORIA", "MARCA", "PRECO", "CUSTO", "ESTOQUE_ATUAL"])
            for p in produtos:
                writer.writerow([p.id, p.nome_produto, p.categoria, p.marca, p.preco, p.custo, p.estoque_atual])