# faça um programa que leia 3 números e informe qual o maior e qual o menor
a = int(input('Digite um número'))
b = int(input('Digite um número'))
c = int(input('Digite um número'))
if a > b > c:
    print(f'O maior número é {a} e o menor número é {c}')
if a > c > b:
    print(f'O maior número é {a} e o menor número é {b}')
if b > a > c:
    print(f'O maior número é {b} e o menor número é {c}')
if b > c > a:
    print(f'O maior número é `{b} e o menor número é {a}')
if c > a > b:
    print(f'O maior número é {c} e o menor número é {b}')
if c > b > a:
    print(f'O maior número é {c} e o menor número é {a}')
