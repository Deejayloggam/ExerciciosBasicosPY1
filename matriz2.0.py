from random import randint
# crie um programa que produza uma matriz de dimensão 3x3 e preencha com valores
# ''lidos pelo teclado'' no final mostre a matriz na tela com a formatação correta
# no final mostre: A soma de todos os valores pares, a soma dos valores da terceira coluna, o maior valor da linha 2
lista = [[randint(1, 10)], [randint(1, 10)], [randint(1, 10)], [randint(1, 10)], [randint(1, 10)], [randint(1, 10)],
         [randint(1, 10)], [randint(1, 10)], [randint(1, 10)]]
soma_pares = 0
copy2 = lista[3:6]
copy2.sort()
print(f'{lista[0:3]}\n{lista[3:6]}\n{lista[6:]}')
for a in range(0, 9):
    if lista[a][0] % 2 == 0:
        soma_pares += lista[a][0]
print(f'A soma de todos os valores pares é: {soma_pares}')
print(f'A soma dos valores da terceira coluna é: {lista[8][0] + lista[5][0] + lista[2][0]}')
print(f'O maior valor da segunda linha é: {copy2[2][0]}')
