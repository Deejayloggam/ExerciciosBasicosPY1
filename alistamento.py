# faça um programa que leia o ano de ascimento de um jovem e informe de acordo com sua idade:
# Se ele ainda vai se alistas ao serviço militar,
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
a = int(input('Qual seu ano de nascimento?'))
if 2021-a < 18:
    print(f'Ainda não está no momento de alistamento, faltam {18-2021-a} anos')
elif 2021-a == 18:
    print('Está no momento de se alistar')
else:
    print(f'Já se passaram {2021-a-18} anos do momento de alistamento')
