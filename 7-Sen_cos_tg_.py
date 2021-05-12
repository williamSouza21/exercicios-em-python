from math import radians, sin, cos, tan
ângulo = float(input("Digite o ângulo em graus: "))

seno = sin(radians(ângulo))
print("O seno de {} é {:.2f}".format(ângulo, seno))
cosseno = cos(radians(ângulo))
print("O cosseno de {} é {:.2f}".format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print("A tangente de {} é {:.2f}".format(ângulo, tangente))


# Caso a gente não importasse as funções radians, sin, cos e tan
# da biblioteca math, o código ficaria assim:

# import math
# seno = math.sin(radians(ângulo))
# print("O seno de {} é {:.2f}".format(ângulo, seno))
# cosseno = math.cos(radians(ângulo))
# print("O cosseno de {} é {:.2f}".format(ângulo, cosseno))
# tangente = math.tan(radians(ângulo))
# print("A tangente de {} é {:.2f}".format(ângulo, tangente))
