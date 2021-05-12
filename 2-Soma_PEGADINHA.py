# CUIDADO!!!!!!!!!
# A função input sempre retorna uma string (texto), por isso devos utilizar
# a função int para converter o número digitado de texto para inteiro.
valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))
soma = valor1 + valor2
print("A soma de {} com {} é igual a {}".format(valor1, valor2, soma))

# Se caso não tivermos definio a variável primitiva, o resultado seria uma
# concatenação dos dois valores digitados pelo usuário.
# Ex.: valor1 = 3 e valor2 = 4
# Será printado na tela: A soma de 3 com 4 é igual a 34
