# crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome santo
a = input('Digite o nome de uma cidade\n')
a = a.split()
print("SANTO" in a[0].upper())
