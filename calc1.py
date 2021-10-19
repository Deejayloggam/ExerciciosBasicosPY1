from time import sleep
# crie um programa que leia 2 valores e mostre um menu na tela: [1] somar [2] multiplicar [3] maior [4] novos numeros
# [5] sair do programa; o programa ira realizar cada uma das operações
menu = int
a = int(input('----------CALCULADORA----------\nDIGITE DOIS NÚMEROS:\n'))
b = int(input())
while menu != 5:
    menu = int(input('----menu----\n[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NUMEROS\n[5]SAIR DO PROGRAMA'))
    if menu == 1:
        print(f'-------\n{a+b}')
    if menu == 2:
        print(f'-------\n{a*b}')
    if menu == 3:
        if a > b:
            print(f'O maior número é {a}')
        else:
            print(f'O maior número é {b}')
    if menu == 4:
        a = int(input('\nDIGITE DOIS NÚMEROS:\n'))
        b = int(input())
    if menu > 5:
        for a in range(0, 3):
            sleep(1)
            print('.')
