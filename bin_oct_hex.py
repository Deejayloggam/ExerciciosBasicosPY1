# escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal
a = int(input('Digite um número qualquer'))
b = int(input('Escolha uma base para conversão\n1--Binário\n2--Octal\n3--Hexadecimal'))
if b == 1:
    print(bin(a))
elif b == 2:
    print(oct(a))
elif b == 3:
    print(hex(a))
