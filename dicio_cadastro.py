# crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre: A) quantas pessoas foram cadastradas B) A média de idade do gp
# c) uma lista com todas as mulheres d) uma lista com todas as pessoaas com idade acima da média
geral = []
soma = 0
mulheres = []
acimadamedia = []
while True:
    dicio = {'Nome': input('Nome: '),
             'Sexo': input('Sexo [M/F]: '),
             'Idade': int(input('Idade: '))}
    while dicio['Sexo'] not in 'MmFf':
        print('VERIFIQUE OS DADOS E TENTE NOVAMENTE')
        dicio = {'Nome': input('Nome: '),
                 'Sexo': input('Sexo [M/F]: '),
                 'Idade': int(input('Idade: '))}
    soma += dicio['Idade']
    geral.append(dicio.copy())
    menu = int(input('[0] sair\n[1] continuar'))
    if menu == 0:
        break
for b in geral:
    if b['Sexo'] in 'Ff':
        mulheres.append(b['Nome'])
    if b['Idade'] > soma/len(geral):
        acimadamedia.append(b['Nome'])
print(f'Foram cadastrados {len(geral)} pessoas')
print(f'Média de idade: {soma/len(geral)}')
print(f'Mulheres: {mulheres}')
print(f'Pessoas acima da média: `{acimadamedia}')
