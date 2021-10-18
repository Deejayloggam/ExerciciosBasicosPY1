# faça um programa que leia um número inteiro e diga se ele é ou não um número primo
a = int(input('Digite um número inteiro para informar se o mesmo é primo: '))
b = 0
if a == 2 or a == 3 or a == 5 or a == 7:
    print('É um número primo')
else:
    for c in range(2, 10):
        if a % c == 0:
            b += 1
if b == 0:
    print('É um número primo')
else:
    print('Não é um número primo')
