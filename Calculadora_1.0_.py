valor1 = float(input("Digite o 1° valor: "))
valor2 = float(input("Digite o 2° valor: "))

print("Operações matemáticas da calculadora: ")
print("1- Adição")
print("2- Subtração")
print("3- Multiplicação")
print("4- Divisão")
print("5- Potenciação")
print("6- Radiciação")
operação = int(input("Escolha a operação: "))
if(operação == 1):
    soma = valor1 + valor2
    print("{} + {} = {:.2f}".format(valor1, valor2, soma))
elif(operação == 2):
    subtração = valor1 - valor2
    print("{} - {} = {:.2f}".format(valor1, valor2, subtração))
elif(operação == 3):
    multiplicação = valor1 * valor2
    print("{} * {} = {:.2f}".format(valor1, valor2, multiplicação))
elif(operação == 4):
    divisão = valor1 / valor2
    print("{} / {} = {:.2f}".format(valor1, valor2, divisão))
elif(operação == 5):
    potenciação = pow(valor1, valor2)
    print("{} ^ {} = {:.2f}".format(valor1, valor2, potenciação))
elif(operação == 6):
    radiciação = pow(valor1, 1/2)
    print("A raiz quadrada de {} é {:.2f}".format(valor1, radiciação))
else:
    print("Operação inválida!")
