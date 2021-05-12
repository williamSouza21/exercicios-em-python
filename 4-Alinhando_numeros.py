num = int(input("Digite um número para ver a sua tabuada: "))
i = 1
while(i <= 10):
    print("{} x {:2} = {}".format(num, i, num*i))
    i = i + 1

# O {:2} signica que o número vai ocupar o espaço de 2 números.
# Ex.: Se num = 5
# 5 x  8 = 40
# 5 x  9 = 45
# 5 x 10 = 50

# O 8 e 9 ficaram alinhados com o 10!
