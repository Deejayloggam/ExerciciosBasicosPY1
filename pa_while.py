from time import sleep
# MOSTRE OS X PRIMEIROS TERMOS DE UMA PA USANDO WHILE
primeiro_termo = int(input('Digite o primeiro termo da PA\n'))
razao = int(input('Digite a razão da PA\n'))
termos = int(input('Digite quantos termos você quer observar\n'))
cont = 0
while termos != cont:
    print(f'{primeiro_termo+razao*cont}', end='->')
    cont += 1
    sleep(0.5)
print('...')
