



lista = ['Guerreiro', 
         'Mago', 
         'Arqueiro', 
         'Ladino', 
         'Clérigo', 
         'Paladino', 
         'Bárbaro', 
         'Druida', 
         'Feiticeiro', 
         'Monge', 
         'Necromante', 
         'Cavaleiro', 
         'Elementalista', 
         'Artesão', 
         'Mercenário', 
         'Caçador de recompensas', 
         'Assassino', 
         'Guardião', 
         'Templário', 
         'Xamã']


def escolher_classe(lista):

    for i, elemento in enumerate(lista):
        print(f"{i+1}. {elemento}")
    
    escolha = input("\n\nDigite o número da opção desejada: \n\n")
    escolha_int = int(escolha)
    
    if escolha_int < 1 or escolha_int > len(lista):
        print("Opção inválida!")
    else:
        escolha_index = escolha_int - 1
        escolha_elemento = lista[escolha_index]
        print(f"\n\nVocê escolheu: {escolha_elemento}\n\n")
    return escolha_elemento


escolher_classe(lista) 