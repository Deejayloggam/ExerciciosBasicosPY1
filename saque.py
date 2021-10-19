# crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
# a ser sacado e o programa vai informar quantas cédulas de cada valor serão entregues.
# Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
a = int(input('VALOR DO SAQUE: '))
cinquenta = 0
vinte = 0
dez = 0
um = 0
while True:
    if a >= 50:
        a -= 50
        cinquenta += 1
    elif 50 > a >= 20:
        a -= 20
        vinte += 1
    elif 20 > a >= 10:
        a -= 10
        dez += 1
    elif 10 > a >= 1:
        a -= 1
        um += 1
    else:
        break
print(f'{cinquenta} notas de R50\n{vinte} notas de R$20\n{dez} notas de R$10\n{um} notas de R$1')
