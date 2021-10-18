# faça um programa que leia um número inteiro e diga se ele é ou não um número primo
a = int(input('Digite um número inteiro para informar se o mesmo é primo: '))
b = 0
for c in range(1, a+1):
    if a % c == 0:
        b += 1
if b > 2:
    print('Não é primo ')
else:
    print('É um número primo')
