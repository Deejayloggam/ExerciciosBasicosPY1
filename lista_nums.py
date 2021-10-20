from random import randint
# crie um programa que leia vários números e coloque-os em uma lista. Depois mostre: A) quantos numeros foram digitados
# B) A lista de valores, ordenada de forma decrescente C) Se o valor 5 foi digitado e está ou não na lista
lista = []
while True:
    a = randint(0, 10)
    print(a)
    lista.append(a)
    r = input('Quer continuar? [S/N]')
    while r not in 'SsNn':
        r = input('INVALIDO - Quer continuar? S/N')
    if r in "nN":
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} valores\nA lista de valores em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 foi digitado')
else:
    print('Não há valor 5')
