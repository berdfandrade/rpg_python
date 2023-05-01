


class item:
    def __init__(self, nome, descricao, peso, preco, quantidade):
        self.nome = nome
        self.quantidade = quantidade
        self.peso = peso
        self.preco = preco
        self.descricao = descricao

    def __str__(self):
        return  f"\nItem: {self.nome} \nDescrição {self.descricao} \nPeso: {self.peso} \nPreço: {self.preco}"  

boneDoMst = item("Boné do MST", "Um bone contra a propriedade privada dos meios de produção", 1, 0.1, 0)       

print(boneDoMst)


