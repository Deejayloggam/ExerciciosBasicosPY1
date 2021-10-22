# faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações: - quantidade de notas - a maior nota - a menor nota - a média da turma
# - a situação (opcional)

def notas(*notas, sit=True):
    qtd = len(notas)
    media = sum(notas)/len(notas)
    menor = sorted(notas)[0]
    maior = sorted(notas)[-1]
    situacao = str
    print(media, qtd, maior, menor)
    dicio = {'Total': qtd,
             'Maior': maior,
             'Menor': menor,
             'Média': media
             }
    if media > 7.0:
        situacao = 'BOA'
    elif 5.0 <= media <= 7.0:
        situacao = 'REGULAR'
    else:
        situacao = 'RUIM'
    if sit:
        dicio['Situação'] = situacao
    return dicio


resp = notas(3.5, 2, 6.5)
print(resp)
