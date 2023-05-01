


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

class jogador:

    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.dinheiro = 2000
        self.exp = 0
        self.level = 5
        self.ataque = 300
        self.defesa = 300
        self.inventario = {}

    def atacar(self):
        print(f"{self.nome} atacou!")

    def defender(self):
        print(f"{self.nome} defendeu!")

    def mover(self):
        print(f"{self.nome} se moveu")

    def ganhar_experiencia(self, experiencia_ganha):
        self.exp += experiencia_ganha
        print(f"{self.nome} ganhou {experiencia_ganha} exp")

    def pegar_itens(self, *itens):
        for item in itens:
            if item.nome in self.inventario:
                self.inventario[item.nome].append(item)
            else:
                self.inventario[item.nome] = [item]
                
    def __str__(self):
        return f"{self.nome} está no level {self.level} | ATK: {self.ataque} | DEF: {self.defesa} |"

    def mostrar_inventario(self):
        return self.inventario



bernardo = jogador("Bernardo", "Druida")
bernardo.pegar_itens(boneDoMst)

print(bernardo)
print(bernardo.mostrar_inventario()) 
