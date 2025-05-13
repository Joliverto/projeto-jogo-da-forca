import random as rd

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
print("Bem-vindo(a) ao jogo da forca!")
print("Adivinhe a palavra abaixo:")

# Armazena a palavra escolhida aleatoriamente
palavra_escolhida = rd.choice(palavras)

# Armazena a palavra de forma mascarada
# palavra_oculta = crialinha(palavra_escolhida)
palavra_oculta_lista = ["_" for i in palavra_escolhida]
palavra_oculta = "".join(palavra_oculta_lista)
print(palavra_oculta)

##########################################

# While onde irá continuar perguntando até que...
letras_erradas = []
chances = 6
while chances != 0:

    # Mostra os pontos do usuário
    print("Chances restantes: {}".format(chances))
    print("Letras erradas: {}".format(letras_erradas))

    # Pede a letra para arriscar e verifica se ela é válida
    letra = str(input("Digite uma letra: ")).lower()
    while (len(letra) == 0) or (len(letra)) > 1 or (letra.isnumeric()):
        print("Você deve digitar apenas uma letra!")
        letra = str(input("Digite uma letra: "))

    # Verifica se existe a letra na palavra
    if letra not in palavra_escolhida:
            chances -= 1
            letras_erradas.append(letra)
    else:
        # Verifica quantas letras tem na palavra e converte
        for indice, caractere in enumerate(palavra_escolhida):
            if caractere == letra:
                palavra_oculta_lista[indice] = letra

            

            
    print("".join(palavra_oculta_lista))



