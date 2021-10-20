# crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# caso o numero já exita lá dentro, ele não será adicionado, no final serão exibidos todos os valores únicos digitados
# em ordem crescente.
lista = []
while str not in lista:
    lista.append(int(input('Digite um número [999 p/ sair]\n')))
    if lista[-1] == 999:
        del lista[-1]
        break
    for a in lista[:-1]:
        if lista[-1] == a:
            del lista[-1]
            print('Este número já existe')
print(f'Os números digitados em ordem crescente foram : {lista}')
