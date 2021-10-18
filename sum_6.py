# desenvolva um programa que leia 6 números inteiros e mostre apenas a soma daqueles que forem pares. Se o valor
# digitado for ímpar, desconsidere-o
b = 0
for c in range(1, 7):
    a = int(input('Digite um número: '))
    if a%2 == 0:
        b += a
print(b)
