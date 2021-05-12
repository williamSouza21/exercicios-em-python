# Para o N° ser primo, ele deve ser divisível por 1 e por ele mesmo (divisível 2 vezes).
número = int(input("Digite um número: "))
total = 0
for contador in range(1, número+1):
    if(número % contador == 0):
        print("\033[33m", end=" ")
        total += 1
    else:
        print("\033[31m", end=" ")

    print("{}  ".format(contador), end=" ")

print("\n \033[m")
print(("O número {} foi divisível {} vezes.".format(número, total)))
if(total == 2):
    print("E por isso ele É PRIMO!")
else:
    print("E por isso ele NÃO É PRIMO!")
# Se o número = 5, será printado na tela:
# 1   2   3   4   5

# O end=" " faz com que os valores sejam printados na horizontal (não pulam linha).

# \033[33m faz com que o próximos print sejam AMARELOS
# \033[31m faz com que o próximos print sejam VERMELHOS
# \033[m faz com que os próximos prints sejam BRANCOS
