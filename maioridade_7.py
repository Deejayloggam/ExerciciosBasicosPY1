# crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores.
a = 0
for c in range(1, 8):
    b = int(input('Digite a idade da pessoa desejada: '))
    if b >= 18:
        a += 1
print(f'Número de maiores: {a}\nNúmero de menores: {7-a}')
