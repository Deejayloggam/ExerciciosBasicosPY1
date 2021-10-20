from random import randint
# faça um programa que crie palpites para a mega sena, perguntando o numero de jogos a ser gerados.
a = int(input('Quantos jogos serão gerados?'))
jogos = []
jogo = []
for b in range(0, a):
    while len(jogo) < 6:
        d = randint(1, 60)
        if d not in jogo:
            jogo.append(d)
    jogos.append(jogo[:])
    jogo.clear()
for z in range(0, a):
    print(sorted(jogos[z]))
