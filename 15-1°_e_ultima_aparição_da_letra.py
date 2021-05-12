frase = str(input("Digite uma frase: ")).upper().strip()
print("A letra A aparece {} vezes na frase".format(frase.count("A")))
# O .count("") conta quantos caracteres iguais aos declarados
# dentro das aspas há na string (no caso dessa qustão, caractere = A).
print("A 1° letra A aparece na posição {}".format(frase.find("A")+1))
print("A última letra A aparece na posição {}".format(frase.rfind("A")+1))

# .find("A") fornece a posição do 1° A que ele encontra na string.
# .rfind("A") fornece a posição do 1° A que ele encontra começando pela direita (último A).
