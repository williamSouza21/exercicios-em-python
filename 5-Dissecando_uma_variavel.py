variavel = input("Digite algo: ")
print("O tipo primitivo desse valor é ", type(variavel))
print("Só tem espaços? ", variavel.isspace())
print("É um número? ", variavel.isnumeric())
print("É formado somente por letras? ", variavel.isalpha())
print("É formado por letras e números? ", variavel.isalnum())
print("É formado somente por letras maiúsculas? ", variavel.isupper())
print("É formado somente por letras minúsculas? ", variavel.islower())