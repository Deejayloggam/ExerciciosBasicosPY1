from math import hypot
# realize um programa que leia o comprimento do cateto oposto e do adjacente de um triângulo retângulo e calcule a
# hipotenusa
a = float(input('Digite o valor do cateto adjacente '))
b = float(input('Digite o valor do cateto oposto '))
print(f'O valor da hipotenusa é {hypot(a, b)}')
