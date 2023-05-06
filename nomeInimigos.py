


import random


def gerar_nome_vilao():
    vogais = ['a', 'e', 'i', 'o', 'u']
    consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'w', 'y', 'z']
    nome = ''
    for i in range(random.randint(2, 9)):
        if i % 2 == 0:
            nome += random.choice(consoantes)
        else:
            nome += random.choice(vogais)
    return nome.title()


def nomesBolados():
    for i in range(150):
        print(gerar_nome_vilao())

