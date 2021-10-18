# faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no
# intervalo de 1 até 500
b = 0
for c in range(3, 500, 3):
    if c%2 != 0:
        b += c
print(b)
