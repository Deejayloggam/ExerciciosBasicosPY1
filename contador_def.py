from time import sleep
# faça um programa que tenha uma função chamada contador(), que receba três parametros: inicio, fim e passo e realize a
# contagem. Seu programa tem que realizar três contagens através da função criada: a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2, c) uma contagem personalizada


def contador(a, b, c):
    if a < b:
        for a in range(a, b + 1, c):
            print(a)
            sleep(1)
    if a > b:
        for a in range(a, b - 1, c):
            print(a)
            sleep(1)


contador(1, 10, 1)
contador(10, 0, -2)
contador(int(input('INICIO: ')), int(input('FIM: ')), int(input('PASSO: ')))
