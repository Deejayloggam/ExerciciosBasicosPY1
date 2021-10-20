# crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
# individualmente
print('------- SISTEMA ESCOLAR -------')
cont = -1
geral = []
while True:
    aluno = input('NOME: ').upper()
    nota1 = float(input('NOTA 1: '))
    nota2 = float(input('NOTA 2: '))
    cont += 1
    geral.insert(cont, [aluno, nota1/nota2])
    menu = input('continuar [S/N]: ')
    if menu in 'Nn':
        break
print(geral)
while True:
    menu = input('Digite o nome de um aluno para ver individualmente ou N para sair:')
    if menu in 'Nn':
        break
    else:
        for h in geral:
            if h[0] == menu.upper():
                print(h)
