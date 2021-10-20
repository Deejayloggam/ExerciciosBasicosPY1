from random import randint
# crie um programa onde o 'usuário' possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
c = []
pares = []
impares = []
for a in range(0, 7):
    print('Digite um número: ')
    b = randint(1, 100)
    print(b)
    if b % 2 == 0:
        pares.insert(0, b)
    else:
        impares.insert(0, b)
pares.sort()
impares.sort()
c.insert(0, pares)
c.insert(1, impares)
print(c)
