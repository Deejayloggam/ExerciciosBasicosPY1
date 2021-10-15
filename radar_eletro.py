# escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar R$7,00 por cada KM acima do limite
a = int(input('Com quantos KM o carro passou?'))
if a > 80:
    print(f'VOCÊ FOI MULTADO\nValor da multa: R${(a-80)*7}')
