# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atle e mostre a sua
# categoria, de acordo com a idade
# até 9 anos: MIRIM
# até 14 anos: INFANTIL
# até 19 anos: JUNIOR
# até 20 anos: Sênior
# acima: MASTER
a = int(input('Digite a idade do atleta: '))
if a <= 9:
    print('MIRIM')
elif 9 < a <= 14:
    print('INFANTIL')
elif 14 < a <= 19:
    print('JUNIOR')
elif 19 < a <= 20:
    print('SÊNIOR')
elif 20 < a:
    print('--MASTER--')
