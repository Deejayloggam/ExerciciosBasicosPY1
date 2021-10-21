from datetime import datetime
# crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionario
# se por acaso CTPS for diferente de 0, o dicionario receberá também o ano de contratação e o salário. Calcule e
# acrescente, além da idade, com quantas anos a pessoa vai se aposentar.
pessoa = {'Nome': input('Nome: '),
          'Ano de nascimento': int(input('Ano de nascimento: ')),
          'CTPS': int(input('CTPS: '))}
pessoa['Idade'] = datetime.now().year - pessoa['Ano de nascimento']
if pessoa['CTPS'] != 0:
    pessoa['Ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: '))
    pessoa['Aposentadoria'] = pessoa['Idade'] + (datetime.now().year - pessoa['Ano de contratação'])
for k, v in pessoa.items():
    print(f'{k} - {v}')
