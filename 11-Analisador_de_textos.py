nome = str(input("Digite o seu nome: ")).strip()
print("Analisando o seu nome...")
print("O seu nome em letras maiúsculas é {}".format(nome.upper()))
print("O seu nome em letras minúsculas é {}".format(nome.lower()))
print("O seu nome ao todo tem {} letras".format(len(nome) - nome.count(" ")))
# print("O seu primeiro nome tem {} letras".format(nome.find(" ")))

separa = nome.split()
print("O seu primeiro nome é {} e ele tem {} letras".format(
    separa[0], len(separa[0])))

# O .strip() elimina os espaços antes e depois dos nomes, mas não elimina
# os espaços entre os nomes.

# A função len() conta quantos carateres há na string (retorna o tamanho da string).
# O .count(" ") conta quanto espaços há entre os nomes.

# O .find(" ") lê a string até encontrar o primeiro caractere declarado
# dentro das aspas (nese caso o espaço) e retorna a quantidade de caracteres lidos.

# O .split() coloca cada um dos nomes como itens de uma lista.
# Ex.: nome = william de souza
# separa = ["william", "de", "souza"]
