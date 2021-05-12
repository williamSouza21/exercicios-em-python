# Utilizando separador de strings e eliminador de espaços:
expressão = str(input("Digite uma expressão matemática: ")).strip()

# SOMA
if(("+" in expressão) == True):
    posição = int(expressão.find("+"))
    soma = int(expressão[posição-1]) + int(expressão[posição+1])
    print("{} + {} = {}".format(separa[0], separa[2], soma))
# SUBTRAÇÃO
elif(("-" in separa) == True):
    subtração = int(separa[0]) - int(separa[2])
    print("{} - {} = {}".format(separa[0], separa[2], subtração))
# Multiplicação
elif(("*" in separa) == True):
    multiplicação = int(separa[0]) * int(separa[2])
    print("{} * {} = {}".format(separa[0], separa[2], multiplicação))
# Divisão
elif(("/" in separa) == True):
    divisão = int(separa[0]) / int(separa[2])
    print("{} / {} = {}".format(separa[0], separa[2], divisão))
