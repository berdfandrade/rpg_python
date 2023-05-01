


class Guerreiro:
    def __init__(self):
        self.nome = "Guerreiro"
        self.vida = 1000
        self.forca = 100
        self.defesa = 80
        self.agilidade = 5
        self.inteligencia = 50

    def __str__(self):
        return f" \nVida: {self.vida}\nForça: {self.forca}\nDefesa: {self.defesa}\nAgilidade: {self.agilidade}\nInteligencia: {self.inteligencia}"

class Mago:
    def __init__(self):
        self.nome = "Mago"
        self.vida = 800
        self.forca = 50
        self.defesa = 80
        self.agilidade = 80
        self.inteligencia = 150

    def __str__(self):
        return f" \nVida: {self.vida}\nForça: {self.forca}\nDefesa: {self.defesa}\nAgilidade: {self.agilidade}\nInteligencia: {self.inteligencia}"        

class Arqueiro:
    def __init__(self):
        self.nome = "Arqueiro"
        self.vida = 90
        self.forca = 7
        self.defesa = 6
        self.agilidade = 10
        self.inteligencia = 80

    def __str__(self):
        return f" \nVida: {self.vida}\nForça: {self.forca}\nDefesa: {self.defesa}\nAgilidade: {self.agilidade}\nInteligencia: {self.inteligencia}"
        
class Clerigo:
    def __init__(self):
        self.nome = "Clérigo"
        self.vida = 90
        self.forca = 5
        self.defesa = 8
        self.agilidade = 7
        self.inteligencia = 120

    def __str__(self):
        return f" \nVida: {self.vida}\nForça: {self.forca}\nDefesa: {self.defesa}\nAgilidade: {self.agilidade}\nInteligencia: {self.inteligencia}"
    
class Assassino:
    def __init__(self):
        self.nome = "Assassino"
        self.vida = 90
        self.forca = 5
        self.defesa = 8
        self.agilidade = 7
        self.inteligencia = 70

    def __str__(self):
        return f" \nVida: {self.vida}\nForça: {self.forca}\nDefesa: {self.defesa}\nAgilidade: {self.agilidade}\nInteligencia: {self.inteligencia}"

def escolher_classe():
    print("Escolha sua classe:")
    print("1. Guerreiro")
    print("2. Mago")
    print("3. Arqueiro")
    print("4. Clérigo")
    print("5. Assassino")

    escolha = int(input("Digite o número da sua escolha: "))

    if escolha == 1:
        return Guerreiro()
    elif escolha == 2:
        return Mago()
    elif escolha == 3:
        return Arqueiro()
    elif escolha == 4:
        return Clerigo()
    elif escolha == 5:
        return Assassino()
    else:
        print("Opção inválida, escolha novamente.")
        return escolher_classe()

personagem = escolher_classe()
print(f"\nVocê escolheu ser um {personagem.nome}\n\nATRIBUTOS: \n {personagem}\n")

