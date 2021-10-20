from random import randint  
# crie um programa que produza uma matriz de dimensão 3x3 e preencha com valores
# ''lidos pelo teclado'' no final mostre a matriz na tela com a formatação correta
lista = [[randint(1, 10)], [randint(1, 10)], [randint(1, 10)], [randint(1, 10)], [randint(1, 10)], [randint(1, 10)],
         [randint(1, 10)], [randint(1, 10)], [randint(1, 10)]]
print(f'{lista[0:3]}\n{lista[3:6]}\n{lista[6:]}')
