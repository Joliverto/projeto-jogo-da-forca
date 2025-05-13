letra = str(input("Digite uma letra: "))
while (len(letra) == 0) or (len(letra)) > 1 or (letra.isnumeric):
    print("Você deve digitar apenas uma letra!")
    letra = letra = str(input("Digite uma letra: "))

print("funcionou")


#if (len(letra) == 0) or (len(letra) > 1 or (letra.isnumeric)):
    #print("digite uma string")



# while len(palavra) == 0:
#     if len(palavra) == 0:
#         print("Digita algo ai krl")

# else:
#     while "_" in palavra:
#         print("funcina")
#         a = input("Digite outra palavra: ")
#         if "_" in a:
#             continue
#         else:
#             print("Parabens, a palavra é {}".format(a))
#             break
