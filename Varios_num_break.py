# crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999
# No final mostre quantos numeros foram digitados e a soma entre eles desconsiderando 999 (usando break)
soma = 0
cont = 0
while True:
    n = int(input('Digite um número [999 - PARAR]: '))
    if n == 999:
        break
    soma += n
    cont +=1
print(f'Foram digitados {cont} números e a soma foi {soma}')
