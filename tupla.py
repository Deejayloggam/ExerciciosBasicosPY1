# desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# a) quantas vezes apareceu o valor 9 b) em que posição foi digitado o primeiro valor 3 c) quais foram os numeros pares
a = int(input('Digite 4 valores\n')), int(input()), int(input()), int(input())
pares = []
if a.count(9) > 0:
    print(f'O valor 9 apareceu {a.count(9)} vezes')
else:
    print('Não há valor 9')
if a.count(3) > 0:
    print(f'O primeiro valor 3 apareceu no indice {a.index(3)}')
else:
    print('Não há valor 3')
for b in a:
    if b % 2 == 0:
        pares.append(b)
if not pares:
    print('Não há números pares')
else:
    print('Os pares são: ', pares)
