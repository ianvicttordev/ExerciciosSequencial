# 12 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
#  (72.7*altura) - 58

print("##### PESO IDEAL #####")

altura = float(input("Qual a sua altura?--> "))
resultado = (72.7 * altura) - 58

print(f"Seu peso ideal é {resultado:.3f} KG.")