


# Classe base 
    
class brasileiro:
        def __init__(self, nome):
            self.level = 1
            self.nome = nome
            self.dinheiro = 1320
            self.exp = 0
            self.ataque = 390
            self.defesa = 300
            self.vida = 500
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
            return f"{self.nome} está no level {self.level} | ATK: {self.ataque} | DEF: {self.defesa} | GRANA: {self.dinheiro} |Classe: {type(self).__name__}" 

        def mostrar_inventario(self):
            return f"INVENTÁRIO | {self.inventario}"

        def ver_dinheiro(self):
            return f"DINHEIRO | {self.dinheiro}"


class Capoeirista(brasileiro): #Mestre de Capoeira
    pass

class Sambista(brasileiro): #Mestre Sala 
    pass

class Cangaceiro(brasileiro): # Lampião
    pass  


bernardo = Cangaceiro("Bernardo"); 
print(bernardo)