# faça um programa que leia uma frase pelo teclado e mostre:
# quantas vezes aparece a letra a
# em que posição ela aparece pela primeira vez
# em que posição ela aparece pela última vez
a = input('Digite uma frase')
print(f"A letra 'a' aparece {a.count('a')} vezes")
print('Primeira aparição tem indice', a.find('a'), 'Última aparição', len(a)-1-a[::-1].find('a'))
