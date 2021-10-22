from datetime import datetime
# crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa
# retornando o valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL OU OBRIGATÓRIO nas eleições


def voto(a):
    if 65 > datetime.now().year - a >= 18:
        return 'OBRIGATÓRIO'
    elif 16 <= datetime.now().year - a < 18 or datetime.now().year - a > 65:
        return 'OPCIONAL'
    else:
        return 'NEGADO'


b = voto(int(input('SEU ANO DE NASCIMENTO: ')))
print(f'SEU VOTO É: {b}')
