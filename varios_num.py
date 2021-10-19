# crie um programa que leia vários números inteiros pelo teclado. No final mostre a media deles, qual o menor e o maior
n = int(input('Digige um número: '))
menu = str(input('Quer continuar? [S/N]'))
maior = n
menor = n
soma = n
qtd = 1
while menu.upper() in 'S':
    n = int(input('Digite um número: '))
    soma += n
    qtd += 1
    if maior < n:
        maior = n
    if menor > n:
        menor = n
    menu = str(input('Quer continuar? [S/N]'))
print(f'A média dos valores é {soma/qtd}\nO maior valor é {maior}\nO menor valor é {menor}')
