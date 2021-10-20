from random import randint  # crie um programa que gere cinco numeros aleatorios e coloque em uma tupla.
a = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), )  # Depois mostre a listagem de
print(a)                                                                                # numeros e menor e maior valor
print(f'O menor valor foi {sorted(a)[0]}\nO maior valor foi {sorted(a)[-1]}')
