# 14 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

print('########## CALCULO DE MULTA ##########')

peso_peixe = float(input('Quantos kilos tem o peixe? -->'))
peso_limite = 50 
multa = (peso_peixe - peso_limite) * 4
peso_excesso = (peso_peixe - peso_limite)

if peso_peixe > peso_limite:
    print(f'O peso ultrapassou em {peso_excesso}kg e você terá que pagar uma multa de R$ {multa:.2f}')
else:
    print('NÃO TERÁ MULTA PARA PAGAR')