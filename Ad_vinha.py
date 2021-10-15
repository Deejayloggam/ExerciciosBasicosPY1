from random import randint
# escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa dirá se o usuário venceu ou perdeu
a = randint(1, 5)
b = int(input('Tente acertar o número randomizado: '))
if a == b:
    print('VOCÊ ACERTOU')
else:
    print('você errou')
