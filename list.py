from random import randint  # Crie um programa que lerá varios numeros e colocar em uma lista, deppois disso crie duas
# listas extras, uma que mostre os numeros pares e outra que mostre os numeros impares
print('Quantos numeros você quer digitar?')
c = randint(0, 20)
print(c)
print(f'Digite {c} números')
lista = []
pares = []
impares = []
for a in range(0, c):
    lista.append(randint(0, 10))
    print(lista[-1])
for b in lista:
    if b % 2 == 0:
        pares.append(b)
    else:
        impares.append(b)
print(f'----------\nA lista é : {lista}\nOs pares são {pares}\nOs impares são {impares}')
