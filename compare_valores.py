# escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são igual
a = int(input('Digite o primeito número: '))
b = int(input('Digite o segundo número: '))
if a > b:
    print("O primeiro número é maior")
elif a < b:
    print("O segundo número é maior")
else:
    print('Os valores são iguais')
