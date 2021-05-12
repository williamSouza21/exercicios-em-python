print("-="*20)
print("Analisador de triângulos")
print("-="*20)
a = float(input("Digite o tamanho do 1° lado: "))
b = float(input("Digite o tamanho do 2° lado: "))
c = float(input("Digite o tamanho do 3° lado: "))
# Codição p/ formar triângulos:
# Cada um dos lados deve ser menor que a soma dos outros 2 lados.
if(a < b + c and b < a + c and c < a + b):
    print("Os lados acima formam um triângulo!")
else:
    print("Os lados acima não formam um triângulo!")
