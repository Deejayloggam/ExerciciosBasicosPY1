# faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista, no final mostre:
# a) quantas pessoas foram cadastradas b) uma listagem com as pessoas mais pesadas c) uma com as mais leves
lista = []
maior = 0
menor = 0
nome_pesado = []
nome_leve = []
while True:
    dado = [input('NOME: '), int(input('PESO: '))]
    lista.append(dado[:])
    if maior == 0:  # primeira instancia
        maior = dado[1]
        menor = dado[1]
    if dado[1] > maior:
        maior = dado[1]
    elif dado[1] < menor:
        menor = dado[1]
    menu = input('Quer continuar [S/N]: ')
    if menu in 'Nn':
        break
for g in lista:
    if g[1] == maior:
        nome_pesado.append(g[0])
    if g[1] == menor:
        nome_leve.append(g[0])
print(f'Foram cadastradas {len(lista)} pessoas')
print(f'As pessoas mais pesadas foram: {nome_pesado}')
print(f'As pessoas mais leves foram {nome_leve}')
