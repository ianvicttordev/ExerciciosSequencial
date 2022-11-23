# 13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# A - Para homens: (72.7*h) - 58
# B - Para mulheres: (62.1*h) - 44.7

print("######## PESO IDEAL ########")

sexo = input('De qual sexo deseja saber o peso ideal? h/m: --> ')

if sexo == 'h':
    altura_homem = float(input('Qual a altura: --> '))
    peso_hoje = float(input('Qual seu peso hoje: --> '))
    resultado_homem = (72.7 * altura_homem) - 58
    if peso_hoje > resultado_homem:
        print(f'O seu peso hoje é {peso_hoje}kg e seu peso ideal é {resultado_homem:.2f}kg ')
else:
    altura_mulher = float(input('Qual a altura: --> '))
    peso_hoje_m = float(input('Qual seu peso hoje: --> '))
    resultado_mulher = (62.1 * altura_mulher) - 44.7
    if peso_hoje_m > resultado_mulher:
        print(f'O seu peso hoje é {peso_hoje_m}kg e seu peso ideal é {resultado_mulher:.2f}kg ')