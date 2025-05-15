# Projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão 1

import random as rd
from os import system, name

palavras = [
    "abacaxi",
    "girassol",
    "computador",
    "violão",
    "astronauta",
    "cachorro",
    "planeta",
    "montanha",
    "escola",
    "bicicleta",
    "janela",
    "foguete",
    "elefante",
    "livro",
    "carnaval",
    "oceano",
    "teclado",
    "internet",
    "telefone",
    "dinossauro"
]

# Inicio do jogo
print("")
print("Bem-vindo(a) ao jogo da forca!")
print("Adivinhe a palavra abaixo:")
print("")
print("")

# Armazena a palavra escolhida aleatoriamente
palavra_escolhida = rd.choice(palavras)

# Armazena a palavra de forma mascarada
palavra_oculta_lista = ["_" for i in palavra_escolhida]
palavra_oculta = "".join(palavra_oculta_lista)
print(palavra_oculta)
print("")

# While onde irá continuar perguntando até que...
letras_erradas = []
chances = 6
while chances > 0:

    # Mostra a interface do usuário: Chances e Letras erradas.
    print("Chances restantes: {}".format(chances))
    print("Letras erradas: {}".format(", ".join(letras_erradas)))
    print("")
    print("")

    # Pede a letra para arriscar e verifica se ela é válida
    letra = str(input("Digite uma letra: ")).lower()
    while (len(letra) == 0) or (len(letra)) > 1 or (letra.isnumeric()):
        print("Você deve digitar apenas uma letra!")
        letra = str(input("Digite uma letra: "))
        print("")

    # Verifica se existe a letra na palavra
    if letra not in palavra_escolhida:
            chances -= 1
            letras_erradas.append(letra)
    else:
        # Verifica quantas letras tem na palavra e converte
        for indice, caractere in enumerate(palavra_escolhida):
            if caractere == letra:
                palavra_oculta_lista[indice] = letra

    # Verifica se venceu o desafio, se não venceu, continua...
    if "".join(palavra_oculta_lista) == palavra_escolhida:
         print("")
         print("Você venceu, a palavra era: {}".format(palavra_escolhida))
         print("")
         break
    else:
        print("".join(palavra_oculta_lista))
        print("")

# Mensagem de derrota caso você perca todas as chances
if chances <= 0:
     print("Você perdeu, a palavra era: {}".format(palavra_escolhida))