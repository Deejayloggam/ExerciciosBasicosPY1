from copy import copy
# faça um programa que leia 5 valores numéricos e guarde em uma lista. No final mostre o maior e o menor valor digitado
# e suas respectivas posições em uma lista
lista = [int(input('Digite 5 números')), int(input()), int(input()), int(input()), int(input())]
maior_menor = copy(lista)
indicesmenor = []
indicesmaior = []
print(lista)
for b, a in enumerate(lista):
    if a == maior_menor[0]:
        indicesmenor.append(b)
    if a == maior_menor[4]:
        indicesmaior.append(b)
print(f'O menor valor foi {maior_menor[0]} nos indices: {indicesmenor}')
print(f'O maior valor foi {maior_menor[4]} nos indices: {indicesmaior}')
