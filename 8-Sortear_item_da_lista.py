import random

aluno1 = input("Digite o nome do 1° aluno: ")
aluno2 = input("Digite o nome do 2° aluno: ")
aluno3 = input("Digite o nome do 3° aluno: ")
aluno4 = input("Digite o nome do 4° aluno: ")

lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print("O aluno escolhido foi {}".format(escolhido))

# Caso eu quisesse importar somente a função choice da biblioteca random:

# from random import choice

# aluno1 = input("Digite o nome do 1° aluno: ")
# aluno2 = input("Digite o nome do 2° aluno: ")
# aluno3 = input("Digite o nome do 3° aluno: ")
# aluno4 = input("Digite o nome do 4° aluno: ")

# lista = [aluno1, aluno2, aluno3, aluno4]
# escolhido = choice(lista)
# print("O aluno escolhido foi {}".format(escolhido))
