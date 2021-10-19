# faça um programa que leia o sexo de uma pessoa, mas apenas aceite os valores M ou F, caso esteja errado, peça novament
sexo = str(input('Digite o sexo [M/F]: '))
while sexo not in 'MmFf':
    sexo = input('---TENTE NOVAMENTE---\nDigite o sexo [M/F]: ')
