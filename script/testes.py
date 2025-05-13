palavra = "computador"
espacos = ["_" for i in palavra]
teste = "".join(espacos)
letra = "o"

for i in palavra:
    if i == letra:
        espacos[palavra.index(i)] = i


print(espacos)