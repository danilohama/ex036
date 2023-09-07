""" Escreva um programa para aprovar um empréstimo bancário para comprar uma casa. O programa vai perguntar o valor da
casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então seu empréstimo sera negado
"""
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Em quantos anos deseja quitar o financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa no valor de R${:.2f} em {} anos '.format(casa, anos), end='')
print('a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Empréstimo pode ser \33[0:32mCONCEDIDO!')
else:
    print('Empréstimo \033[0:31mNEGADO!')
