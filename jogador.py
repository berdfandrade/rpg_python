

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
        return f"{self.nome} atacou!"

    def defender(self):
        return f"{self.nome} defendeu!"

    def mover(self):
        return f"{self.nome} se moveu"

    def ganhar_experiencia(self, experiencia_ganha):
        self.exp += experiencia_ganha
        return f"{self.nome} ganhou {experiencia_ganha} exp"

    def pegar_itens(self, *itens):
        for item in itens:
            if item.nome in self.inventario:
                self.inventario[item.nome].append(item)
            else:
                self.inventario[item.nome] = [item]
                
    def __str__(self):
        return f"{self.nome} está no level {self.level} | ATK: {self.ataque} | DEF: {self.defesa} |"

    def mostrar_inventario(self):
        return f"INVENTÁRIO | {self.inventario}"






