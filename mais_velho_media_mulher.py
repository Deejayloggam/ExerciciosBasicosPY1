# desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo
# qual é o nome do homem mais velho.
# Quantas mulheres te menor de 20 anos
idade_do_grupo = 0
nome_homem_mais_velho = str
n_de_mulheres_menos_20 = 0
idade_homem_mais_velho = 0
for z in range(1, 5):
    a = str(input('Digite o nome: '))
    b = int(input('Escolha o sexo:\n[1] Masculino\n[2] Feminino'))
    c = int(input('Digite a idade: '))
    idade_do_grupo += c
    if b == 1:
        if c > idade_homem_mais_velho:
            nome_homem_mais_velho = a
            idade_homem_mais_velho = c
    if b == 2:
        if c < 20:
            n_de_mulheres_menos_20 += 1
print(f'A média de idade do grupo: {idade_do_grupo/4}')
print(f'O nome do homem mais velho: {nome_homem_mais_velho}')
print(f'{n_de_mulheres_menos_20} mulheres tem menos de 20 anos')
