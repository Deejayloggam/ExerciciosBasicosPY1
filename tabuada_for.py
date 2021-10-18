# faça uma tabuada utilizando laço de repetição for
a = int(input('Digite um número para obter sua tabuada: '))
for c in range(1, 11):
    print(f'{a} * {c} = {a*c}')
