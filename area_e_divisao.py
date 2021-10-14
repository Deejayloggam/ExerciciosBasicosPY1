# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m quadrados
altura = float(input('Informa a altura da parede em metros\n'))
largura = float(input('Informe a largura da parede em metros\n'))
print(f'A área da parede é de {altura*largura}\nE a quantidade de tinta necessária para pintar é de {altura*largura/2}')
