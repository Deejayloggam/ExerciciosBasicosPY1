# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário.
desempenho = {'Jogador': input('Nome do jogador: ')}
gols = []
total = 0
n = int(input(f'Quantas partidas {desempenho["Jogador"]} jogou? '))
for a in range(1, n+1):
    b = int(input(f'Quantos gols {desempenho["Jogador"]} fez na partida {a}: '))
    total += b
    gols.append(b)
desempenho['Gols'] = gols
desempenho['Total'] = total
for k, p in desempenho.items():
    print(f'{k} - {p}')
for g in range(1, n+1):
    print(f'Na {g}ª partida fez {desempenho["Gols"][g-1]}')
