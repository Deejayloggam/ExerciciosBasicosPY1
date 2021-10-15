# faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
a = input('Digite um número de 0 a 9999\n')
a = '000' + a
print(f'Milhar: {a[0]}\nCentena: {a[0+1]}\nDezena: {a[0+2]}\nUnidade: {a[0+3]}')
