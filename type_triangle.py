# Refaça o desafio dos triangulos acrescentando o recurso de mostrar qual tipo de triângulo será formado:
# Equilátero: Todos os lados iguais
# Isósceles: Dois lados iguais
# Escaleno: Todos os lados diferentes
a = int(input('Digite o valor da primeira reta: '))
b = int(input('Digite o valor da segunda reta: '))
c = int(input('Digite o valor da terceira reta: '))
if a + b > c and b + c > a and c + a > b:
    print('As retas podem formar um triangulo')
    if a == b == c:
        print('Formará um triangulo equilatero')
    elif a != b and b != c and c != a:
        print('Formará um triangulo escaleno')
    else:
        print('Formará um triangulo isósceles')
else:
    print('Não pode formar um triângulo')
