número = int(input("Digite um número inteiro: "))
print('''Escolha uma das bases para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opção = int(input("A sua opção: "))
if(opção == 1):
    print("{} em binário é {}".format(número, bin(número)[2:]))
if(opção == 2):
    print("{} em octal é {}".format(número, oct(número)[2:]))
if(opção == 3):
    print("{} em hexadecimal é {}".format(número, hex(número)[2:]))
else:
    print("Opção inválida!")


# O [2:] indica que só será mostrado a partir da terceira posição da string
