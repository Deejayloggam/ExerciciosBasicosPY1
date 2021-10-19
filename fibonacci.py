# escreva um programa que leia um numero N inteiro e mostra os N primeiros elementos da sequencia de fibonacci
n = int(input('DIGITE QUANTOS NUMEROS DE FIBONACCI VOCÊ QUER OBSERVAR\n'))
primeiro = 1
segundo = 2
if n == 1:
    print(0)
elif n == 2:
    print('0\n1')
elif n == 3:
    print('0\n1\n1')
else:
    n -= 3
    print('0\n1\n1')
    while n != 0:
        print(primeiro+segundo)
        primeiro = primeiro + segundo
        n -= 1
        print(primeiro+segundo)
        segundo = primeiro + segundo
        n -= 1
