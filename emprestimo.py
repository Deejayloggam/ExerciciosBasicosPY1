# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar:
# o valor da casa
# O salário
# Em quantos anos ele quer pagar
# Calcule o valor da prestação mensal, sabendo que não se pode exceder 30% do salário
valor = float(input('Digite o valor da casa'))
salario = float(input('Digite o seu salário'))
anos = float(input('Digite em quantos anos deseja pagar a casa'))*12
if valor/anos > 0.3 * salario:
    print('Empréstimo recusado')
else:
    print('Empréstimo aceito!')
