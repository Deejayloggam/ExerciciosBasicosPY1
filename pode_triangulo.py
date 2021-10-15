# escreva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo
a = int(input('Digite o valor da primeira reta: '))
b = int(input('Digite o valor da segunda reta: '))
c = int(input('Digite o valor da terceira reta: '))
if a + b > c and b + c > a and c + a > b:
    print('As retas podem formas um triangulo')
else:
    print('Não pode formar um triângulo')
