# faça um programa que leia um número qualquer e mostre seu fatorial
n = int(input('Digite o número para obter seu fatorial: '))
m = n
while m != 1:
    m -= 1
    n *= m
print(f'FATORIAL = {n}')
