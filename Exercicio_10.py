# 10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# F = (C * 1.8) + 32

celsius = float(input("Quantos Graus Celsius deseja transformar em Graus Fahrenheit?"))
resultado = (celsius * 1.8) + 32

print(f"O valor de {celsius}°C é equivalente a {resultado:.2f}°F.")