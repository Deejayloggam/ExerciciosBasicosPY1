# escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento
# para salários superiores a 1250, calcule um aumento de 10%
# para salários inferiores ou iguais, aumento de 15%
a = float(input('Digite seu salário'))
if a > 1250:
    print(f'O seu aumento será de R${0.10*a}')
else:
    print(f'O seu aumento será de R${0.15*a}')
