# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.
a = int(input('Nº de dias de aluguel do carro: '))
b = float(input('Km rodado pelo carro alugado: '))
print(f'O valor total a ser pago é de: {a*60+b*0.15}')
