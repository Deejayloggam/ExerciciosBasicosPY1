# crie um programa que tenha uma tupla preenchida com uma contagem de 0 até 20. Seu programa deverá ser um input
# e mostrar o numero digitado de 0 a 20 por extenso
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
b = ('UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE',
     'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
c = int(input('Digite um número de 1 à 20 para obte-lo por extenso: '))
while c > 20 or c < 0:
     print('INVALIDO')
     c = int(input('Digite um número de 1 à 20 para obte-lo por extenso: '))
print(b[a.index(c)])
