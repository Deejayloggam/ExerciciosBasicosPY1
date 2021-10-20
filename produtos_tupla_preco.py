# crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência
# No final, mostre uma listagem de preços organizando os dados em forma tabular
a = ('Alface', 'R$2,85', 'Cebolas', 'R$4,40', 'Laranja', 'R$4,40')
print('PRODUTO        PREÇO')
for b in range(0, len(a), 2):
    print(f'{a[b]}--------{a[b+1]}')
