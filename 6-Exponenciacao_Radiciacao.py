numero = int(input("Digite um número: "))
quadrado = numero ** 2
cubo = numero ** 3
Raiz = numero ** (1/2)

print("O quadrado de {} é {} \nO cubo de {} é {}".format(
    numero, quadrado, numero, cubo))
print("A raiz quadrada de {} é {:.2f}".format(numero, Raiz))

# O {:.2f} significa que o resultado vai apresentar 2 casas decimais!
# Raiz é uma exponenciação com expoentes fracionários.

# Outra forma de fazer potenciação/ radiciação é
# utilizando a função pow:
# pow(valor, expoente)
