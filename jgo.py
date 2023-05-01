

import pyfiglet
ASCII  = pyfiglet.figlet_format("Benny's World")
print(ASCII)

lista = ['Guerreiro', 
         'Mago', 
         'Arqueiro', 
         'Clérigo', 
         'Paladino', 
         'Bárbaro', 
         'Druida', 
         'Monge', ]


def escolher_classe(lista):

    print("\nQual é a sua classe?\n\n\n")

    for i, elemento in enumerate(lista):
        print(f"{i+1}. {elemento}")
    
    
    escolha = input("\n\nDigite o número da opção desejada:      \n\n")
    escolha_int = int(escolha)

    if escolha_int < 1 or escolha_int > len(lista):
        print("Opção inválida!")

    else:
        
        escolha_index = escolha_int - 1
        escolha_elemento = lista[escolha_index]
        print(f"\n\nVocê escolheu: {escolha_elemento}\n\n")
        return escolha_elemento    

# ===============================================================# 

class jogador:
    def __init__(self, nome, classe):
        self.nome = nome
        self.level = 1
        self.classe = classe

    def level(self):
        print(f"Meu nome é {self.nome}, e meu level é {self.level}")

    def __str__(self):
        return print(jogador.__dict__)  



def criar_jogador():
        
        nome = input("\nQual é o seu nome?  \n\n     ")
        classe = escolher_classe(lista)
        novoJogador = jogador(nome, classe)   
        confirmandoEscolha = input(f"\nSeu nome é {nome} e sua classe é {classe}? (s/n)    \n")

        if not (confirmandoEscolha  == "s" or confirmandoEscolha == "S"):
           
           escolhaAlternativa = input("Deseja alterar o nome ou a classe? (Nome/Classe/Os Dois)").lower()

        if(escolhaAlternativa == "nome"):
                nome = input("\nQual é o seu nome?  \n\n     ")
                novoJogador = jogador(nome, classe)  
        elif(escolhaAlternativa == "classe"):
                 classe = escolher_classe(lista)
                 novoJogador = jogador(nome, classe)  
            

        else:
            print(f"Bem vindo ao mundo de Yorkl, {novoJogador.nome}")

            

criar_jogador()



    

