from random import choice
# Faça um jogo de JO KEN PO com o CPU
a = choice(['PEDRA', 'PAPEL', 'TESOURA'])
b = int(input('JO... KEN... PO\n[1] PEDRA\n[2] PAPEL \n[3] TESOURA\n'))
if a == 'PEDRA' and b == 1 or a == 'PAPEL' and b == 2 or a == 'TESOURA' and b == 3:
    print(f'EMPATE   CPU-{a}')
elif a == 'PEDRA' and b == 3 or a == 'PAPEL' and b == 1 or a == 'TESOURA' and b == 2:
    print(f'VOCÊ PERDEU   CPU-{a}')
elif a == 'PEDRA' and b == 2 or a == 'PAPEL' and b == 3 or a == 'TESOURA' and b == 1:
    print(f'VOCÊ VENCEU   CPU-{a}')
else:
    print('INVALIDO')
