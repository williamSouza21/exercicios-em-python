from random import shuffle

aluno1 = input("Digite o nome do 1° aluno: ")
aluno2 = input("Digite o nome do 2° aluno: ")
aluno3 = input("Digite o nome do 3° aluno: ")
aluno4 = input("Digite o nome do 4° aluno: ")

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print("A ordem de apresentação será:")
print(lista)
