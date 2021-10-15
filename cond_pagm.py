# Elabora um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pag.
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Até 2x no cartão: Preço normal
# 3x ou mais no cartão: 20% de juros
a = float(input('Digite o preço do produto: '))
b = int(input("""SELECIONE A OPÇÂO DE PAGAMENTO
À vista dinheiro/cheque [1]
À vista no cartão [2]
Até 2x no cartão [3]
3x ou mais no cartão [4]\n"""))
if b == 1:
    print(f'O preço será de {a*0.9}')
elif b == 2:
    print(f'O preço será de {a*0.95}')
elif b == 3:
    print(f'O preço será de {a}')
else:
    print(f'O preço será de {a*1.2}')
