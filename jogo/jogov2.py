# Projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão 2

import random as rd
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():

    # Windows
    if name == 'nt':
        _ = system('cls')

    # Mac ou Linux
    else:
        _ = system('clear')

#Função
def game():

    limpa_tela()
    print(("\nBem-vindo(a) ao jogo da forca!"))
    print("Adivinha a palavra abaixo:\n")

    # Lista de palavras para o jogo
    with open("arquivos/palavras_forca.txt", "r", encoding="utf-8") as arquivo:
        palavra_escolhida = [x.strip() for x in arquivo]

    # Escolhe randomicamente uma palavra
    palavra = rd.choice(palavra_escolhida)

    # List comprehension
    letras_descobertas = ['_' for letra in palavra]

    # Numero de chances
    chances = 6

    # Lista para as letras erradas:
    letras_erradas = []

    #
    while chances > 0:

        # Print
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))
        
        # Tentativa
        tentativa = input("\n Digite uma letra: ").lower()

        # Condicional
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else: 
            chances -= 1
            letras_erradas.append(tentativa)
        
        # Condicional
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era: {}".format(palavra))
            break

    # Condicional
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era: {}".format(palavra))

# Bloco main
if __name__ == "__main__":
    game()