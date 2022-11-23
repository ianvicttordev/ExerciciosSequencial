# 16 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
import math

print('############### LOJAS DE TINTAS ###############')

area = float(input('Quantos m² deseja pintar? --> '))

litros = (area / 3) * 1.1
latas = math.ceil(litros / 18)
valor = latas * 18

print(f'A quantidade de latas de tintas que devem ser compradas é {latas:.2f} e o valor total sera: R$ {valor:.2f}')