def questao3(lista):
    soma = 0
    i = 0
    for valor in lista:
        soma = soma + lista[i]
        i = i + 1
    return soma


lista = [1.0, 2.1, 3.0]
soma = questao3(lista)
print("A soma dos números da lista é {}".format(soma))
