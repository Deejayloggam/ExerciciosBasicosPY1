# desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos.
a = int(input('Digite o primeiro termo de uma PA: '))
b = float(input('Digite a razão dessa PA: '))
for c in range(1, 11):
    print(f' o {c}º termo da PA é {a*b*c}')
