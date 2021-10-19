# crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário quer continuar
# No final, mostre: a) qual é o total gasto na compra b) quantos produtos custam mais de 1000 reais
# c) qual é o nome do produto mais barato
nome = str
nomemaisbarato = str
preco = str
soma = 0
maisdemil = 0
barato = 0
while True:
    nome = input('DIGITE O NOME DO PRODUTO: ')
    preco = int(input('DIGITE O PREÇO DO PRODUTO: '))
    if soma == 0:
        barato = preco
        nomemaisbarato = nome
    soma += preco
    if preco > 1000:
        maisdemil += 1
    if preco < barato:
        barato = preco
        nomemaisbarato = nome
    a = input('QUER CONTINUAR? [S/N]')
    if a in 'Nn':
        break
print(f'O total gasto foi {soma}\n{maisdemil} produtos custam mais de 1000 reais\n{nomemaisbarato} foi o mais barato')
