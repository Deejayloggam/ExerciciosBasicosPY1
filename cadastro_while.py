# crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o rpograma deverá perguntar se
# o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos. B) Quantos homens foram cadastrados. C) Quantas mulheres tem menos de 20 anos
maiores = 0
homens = 0
mulhermenos20 = 0
idade = int
sexo = int
while True:
    idade = int(input('DIGITE A IDADE DA PESSOA DESEJADA: '))
    sexo = input('DIGITE O SEXO [M/F]')
    while sexo not in 'FfMm':
        sexo = input('DIGITE UM SEXO VÁLIDO [M/F]')
    if idade > 18:
        maiores += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulhermenos20 += 1
    op = input('Quer continuar? [S/N]')
    while op not in 'SsNn':
        op = input('INVALIDO - Quer continuar? [S/N]')
    if op in 'Nn':
        break
print(f'{maiores} tem mais de 18 anos\n{homens} são homens\n{mulhermenos20} mulheres tem menos de 20 anos')
