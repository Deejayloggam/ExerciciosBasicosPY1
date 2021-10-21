# faça um programa que leia nome e média de um aluno. Guardando a situaçãoo do aluno. Se >7.0 aprovado else: não
aluno = {'aluno': input('Nome: '),
         'média': float(input('Média: '))}
if aluno['média'] >= 7.0:
    aluno['Situação'] = 'APROVADO'
else:
    aluno['Situação'] = 'REPROVADO'
for k, a in aluno.items():
    print(f'{k} - {a}')
