# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do python
# só que fazendo a validaçãoo para acertar apenas um valor numérico


def leiaint():
    while True:
        a = input('Digite um numero: ')
        b = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
             'w', 'x', 'y', 'z']
        contnum = 0
        contlet = 0
        for c in b:
            if c in a:
                contnum += 1
        for e in d:
            if e in a:
                contlet += 1
        if contnum >= 1 and contlet == 0:
            return a
        else:
            print('DIGITE UM NUMERO VALIDO')


A = leiaint()
