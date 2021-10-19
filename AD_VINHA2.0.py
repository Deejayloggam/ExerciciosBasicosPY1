from random import randint  # Crie um jogo onde o deve-se advinhar o número em que o computador 'pensou' usando while
cpu = randint(1, 10)        # apresente ao final quantos palpites foram necessários para vencer
cont = 1
p1 = int(input('EM QUE NÚMERO EU PENSEI?'))
while p1 != cpu:
    cont += 1
    print(f'VOCÊ ERROU - O NÚMERO ERA {cpu}\n-----------tente novamente----------')
    cpu = randint(1, 10)
    p1 = int(input('EM QUE NÚMERO EU PENSEI?'))
print(f'VOCÊ ACERTOU!!! FORAM NECESSÁRIAS {cont} tentativas')
