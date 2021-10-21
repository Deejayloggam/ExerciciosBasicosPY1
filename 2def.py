from random import randint
# faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e soma(Par). A primeira função
# vai sortear 5 numeros e vai colocalos dentro da lista e a segunda função vai mostrar a soma entre todos os valores
# pares sorteados pela função anterior
numeros = list()


def sorteia(lst):
    for a in range(0, 5):
        b = randint(1, 100)
        lst.append(b)
    print(lst)


def somapar(vst):
    somapa = 0
    for n in vst:
        if n % 2 == 0:
            somapa += n
    print(somapa)


sorteia(numeros)
somapar(numeros)
