# 15 -Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# A - salário bruto.
# B - quanto pagou ao INSS.
# C - quanto pagou ao sindicato.
# D - o salário líquido.
# E - calcule os descontos e o salário líquido, conforme a tabela abaixo:
# ########## TABELA ##########
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

print('########## FOLHA DE PAGAMENTO ##########')

salario = float(input('Quanto você ganha por hora? --> '))
hora = int(input('Quantas horas você trabalhou neste mês? --> '))

salario_bruto = salario * hora
ir = salario_bruto * (11/100)
inss = salario_bruto * (8/100)
sindicato = salario_bruto * (5/100)
salario_liquido = salario_bruto - ir - inss - sindicato

print(f'+ Salário Bruto:    R$ {salario_bruto:.2f}''\n'
      f'- IR (11%):         R$ {ir:.2f}''\n'
      f'- INSS (8%):        R$ {inss:.2f}''\n'
      f'- sindicato (5%):   R$ {sindicato:.2f}''\n'
      f'= salário liquido:  R$ {salario_liquido:.2f}')