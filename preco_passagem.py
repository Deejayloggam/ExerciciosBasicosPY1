# Desenvolva um programa que pergunta a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$0,50
# por KM para viagens de até 200Km e R$0,45 para viagens mais longas.
a = float(input("Digite a kilometragem de sua viagem"))
if a <= 200:
    print(f'O valor de sua viagem é de R${0.5*a}')
else:
    print(f'O valor de sua viagem é de R${0.45*a}')
