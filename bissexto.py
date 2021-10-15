# crie um programa que identifique se um ano qualquer é bissexto
ano = int(input('Digite um ano'))
if ano%4 == 0:
    print('É um ano bissexto')
else:
    print('Não é bissexto')
