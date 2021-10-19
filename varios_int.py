# crie um programa que leia vários numeros inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
a = int(input('Digite um número [999 para parar]'))
soma = 0
soma += a
cont = 1
while a != 999:
    a = int(input('Digite um número [999 para parar]'))
    soma += a
    cont += 1
print(f'A foma dos números foi {soma-999} e foram digitado {cont-1} números')
