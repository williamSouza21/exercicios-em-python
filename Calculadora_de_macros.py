print("=============================")
print("====Calculadora de Macros====")
print("=============================")
# Recebendo características físicas e frequência de treino do usuário:
# Estrutura física:
altura = int(input("Digite a sua altura (cm): "))
peso = int(input("Digite o seu peso (kg): "))
idade = int(input("Digite a sua idade (anos): "))
sexo = int(input('''Digite o seu sexo:
[1] Masculino
[2] Feminino '''))
# Atividade cotidiana:
atv_cotidiana = int(input('''Como vc é fora da academia?
[1] Sedentário (maior parte do dia sentado/ trabalho em escritório)
[2] Moderadamente ativo (maior parte do dia caminhando ou fazendo alguma atividade)
[3] Bastante ativo (trabalho braçal/ faz entregas pedalando) '''))
# Sobre Musculação:
freq_musculação = int(
    input("Digite o N° de vezes que vc faz musculação na semana: "))
tempo_musculação = int(input(
    "Quanto tempo dura, em média, o seu treino de musculação (tempo em minutos)? "))
intensidade_musculação = int(input('''Com que intensidade vc treina musculação?
[1] Treino pouco intenso
[2] Treino intenso
[3] Treino como um bodybuilder porra!!! '''))
# Sobre Aeróbico:
freq_aeróbico = int(
    input("Digite o N° de vezes que vc faz aeróbico na semana: "))
tempo_aeróbico = int(input(
    "Quanto tempo dura, em média, o seu treino de aeróbico (tempo em minutos)? "))
intensidade_aeróbico = int(input('''Com que intensidade vc treina aeróbico?
[1] Aeróbico pouco intenso
[2] Aeróbico intenso
[3] Aeróbico muito intenso '''))
# Objetivo:
objetivo = int(input('''Qual é o seu ojetivo?
[1] Hipertrofia
[2] Perder peso '''))
# ----------------------------------------------------------------------------------
# Calculando a Taxa Metabólica Basal (TMB):
# P/ Homens:
if(sexo == 1):
    taxa_met_basal = 66.5 + (13.75 * peso) + (5.0 * altura) - (6.8 * idade)
    print("Sua taxa metabólica basal é {:.2f} kcal".format(taxa_met_basal))
# P/ Mulheres:
else:
    taxa_met_basal = 665.0 + (9.60 * peso) + (1.8 * altura) - (4.7 * idade)
    print("Sua taxa metabólica basal é {:.2f} kcal".format(taxa_met_basal))
# ----------------------------------------------------------------------------------
# Calculando o Gasto Energético com Atividade Física:
# P/ Musculação:
if(intensidade_musculação == 1):
    met_musculação = 4.0
elif(intensidade_musculação == 2):
    met_musculação = 4.5
elif(intensidade_musculação == 3):
    met_musculação = 6.0
gasto_musculação = met_musculação * peso * tempo_musculação/60
# P/ Aeróbico:
if(intensidade_aeróbico == 1):
    met_aeróbico = 5.0
elif(intensidade_aeróbico == 2):
    met_aeróbico = 6.5
elif(intensidade_aeróbico == 3):
    met_aeróbico = 7.0
gasto_aeróbico = met_aeróbico * peso * tempo_aeróbico/60
# Gasto energético cotidiano (fora da academia):
if(atv_cotidiana == 1):
    gasto_cotidiano = 200
elif(atv_cotidiana == 2):
    gasto_cotidiano = 300
elif(atv_cotidiana == 3):
    gasto_cotidiano = 400
# Gasto energético com a atividade física:
gasto_atv_física = gasto_musculação + gasto_aeróbico + gasto_cotidiano
# ----------------------------------------------------------------------------------
# Calculando o Gasto Energético Total Diário:
gasto_total = taxa_met_basal + gasto_atv_física
print("O seu gasto calórico diário é {} kcal".format(gasto_total))
