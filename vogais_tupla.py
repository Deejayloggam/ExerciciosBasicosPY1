# crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, p/ cada
# palavra quais são suas vogais
a = ('VIERNES', 'PATRIMONIO', 'ATIVO', 'PASSIVO', 'ECONOMIA', 'RECEITA')
print(' as vogais em cada palavra foram')
for b in a:
    print(f'As vogais de {b} são:', end=' ')
    if 'A' in b:
        print('a', end=' ')
    if 'E' in b:
        print('e', end=' ')
    if 'I' in b:
        print('i', end=' ')
    if 'O' in b:
        print('o', end=' ')
    if 'U' in b:
        print('u', end=' ')
    print(end='\n')
