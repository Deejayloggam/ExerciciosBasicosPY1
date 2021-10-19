import random
# faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
perdas = 0
wins = 0
while True:
    a = random.choice(['PAR', 'IMPAR'])
    print(f'O COMPUTADOR ESCOLHEU {a}')
    b = int(input('ESCOLHA SEU NÚMERO [1-10]: '))
    c = random.randint(1, 10)
    if a == 'PAR' and (b+c) % 2 == 0:
        perdas += 1
        print(f'VOCÊ PERDEU\nCPU - {c}\n----------')
        break
    if a == 'IMPAR' and (b+c) % 2 != 0:
        wins += 1
        print('VOCÊ VENCEU\nCPU - {c}\n----------')
print(f'VOCÊ VENCEU {wins}x\nVOCÊ PERDEU {perdas}x')
