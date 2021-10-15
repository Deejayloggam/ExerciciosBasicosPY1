# Faça um programa que leia o nome completo de uma pessoa e mostre seu 1º e ultimo nome separadamente
a = input("Digite um nome: ")
a = a.split()
print(f"Primeiro nome: {a[0]}\nÚltimo nome: {a[len(a)-1]}")
