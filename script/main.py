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

# apagar dps
a = "nada"
b = "nada"
# Inicio do jogo
print("Bem-vindo(a) ao jogo da forca!")
print("Adivinhe a palavra abaixo:")

# Armazena a palavra escolhida aleatoriamente
palavra_escolhida = rd.choice(palavras)

# Função para criar as linhas de dica para a palavra
def crialinha(palavra):
    lin = ""
    for i in palavra:
        lin += "_"
    return lin

# Armazena a palavra de forma mascarada
linhas = crialinha(palavra_escolhida)
print(linhas)


##########################################

while "_" in 

# Pede a letra para arriscar
letra = str(input("Digite uma letra: "))

def verificaletra(letra):
    lugar = ""

    while "_" or "" in lugar:
        for i in palavra_escolhida:
            if i == letra:
                lugar += i
            else:
                lugar += "_"
    return lugar



