from random import randint
# crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
jogadores = {'Jogador 01': randint(1, 6),
             'Jogador 02': randint(1, 6),
             'Jogador 03': randint(1, 6),
             'Jogador 04': randint(1, 6)}
for j, d in jogadores.items():
    print(f'{j} - {d}')
b = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)
cont = 0
for a in b:
    cont += 1
    print(f'{cont}º lugar - {a[0]}')
    
