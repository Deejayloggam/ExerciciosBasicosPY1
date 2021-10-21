# crie um programa que tenha uma função chamada area, que receba as dimensões de um terreno e mostre sua area:
def area(a, b):
    print('área = ',a*b)


print('CALC TERRENO')
c = float(input('LARGURA [m]: '))
d = float(input('COMPRIMENTO [m]: '))
area(c, d)
