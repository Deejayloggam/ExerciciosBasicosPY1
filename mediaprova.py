# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
# média atingida:
# Média abaixo de 5.0: Reprovado    Média entre 5.0 e 6.9: recuperação      média 7.0 ou superior: Aprovado
a = float(input('Digite sua nota da 1ª VA'))
b = float(input('Digite sua nota da 2ª VA'))
if (a+b)/2 < 5.0:
    print('Você foi reprovado')
elif 7.0 > (a+b)/2 > 5.0:
    print('RECUPERAÇÃO')
elif 7.0 <= (a+b)/2:
    print('APROVADO')
