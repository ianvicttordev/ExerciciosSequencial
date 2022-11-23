# 8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho_hora = float(input("Qual seu sálario por hora?"))
horas_mes = int(input("Quantas horas você trabalhou?"))
resultado = ganho_hora * horas_mes

print(f"Você trabalhou {horas_mes} horas esté mês e irá ganhar {resultado:.2f}")