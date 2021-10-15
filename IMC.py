# Desenvolva um programa que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre o seu staus de acordo com:
# abaixo de 18.5
# entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: obesidade
# acima de 40: obesidade mórbida
a = float(input('Digite o seu peso: '))
b = float(input('Informe sua altura: '))
IMC = a / (b*b)
if IMC < 18.5:
    print('Abaixo do peso')
elif 18.5 <= IMC < 25:
    print('Peso ideal')
elif 25 <= IMC <= 30:
    print('Sobrepeso')
else:
    print('OBESIDADE MÓRBIDA')
