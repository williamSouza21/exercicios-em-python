# Função que converte decimal fracionário para binário:
def questao1(numero):
    lista = []
    for c in range(0, 50):
        resultado = numero * 2
        if(resultado > 1):
            lista.append(1)
            resultado = resultado - 1
            numero = resultado
        elif(resultado < 1):
            lista.append(0)
            numero = resultado
        else:
            lista.append(1)
            break
    soma = 0
    i = 0
    for valor in lista:
        soma = soma + lista[i]
        i = i + 1
    return soma


numero = float(input("Digite um valor decimal entre 0 e 1: "))
soma = questao1(numero)
print("A soma dos primeiros 50 dígitos do número é {}".format(soma))
