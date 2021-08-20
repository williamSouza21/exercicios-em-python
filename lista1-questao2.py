def questao2(num1, num2, precisao):
    if(abs(num1 - num2) < precisao):
        return True
    else:
        return False


resposta = questao2(0.0, 1e-5, 1e-10)
print(resposta)
