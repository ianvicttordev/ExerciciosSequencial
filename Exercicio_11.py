# 11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# A - o produto do dobro do primeiro com metade do segundo .
# B - a soma do triplo do primeiro com o terceiro.
# C - o terceiro elevado ao cubo.

num_1 = int(input("Digite um número inteiro? -->"))
num_2 = int(input("Digite outro número inteiro? -->"))
num_3 = float(input("Digite um número real? -->"))

resultado_1 = (num_1 * 2) * (num_2 / 2)
resultado_2 = (num_1 * 3) + num_3
resultado_3 = num_3 ** 3

print(f"O produto do dobro do primeiro com metade do segundo é --> {resultado_1}.")
print(f"A soma do triplo do primeiro com o terceiro é --> {resultado_2}.")
print(f"O terceiro elevado ao cubo é --> {resultado_3:.2f}.")