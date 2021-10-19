# crie um tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol
# na ordem de colocação. Depois mostre: A) Apenas os 5 primeiros colocados B) Os ultimos 4 colocados da tabela
# C) Uma lista com os times em ordem alfabética D) Em que posição na tabeçla está o time "chapecoense"
a = ('ATLÉTICO MG', 'FLAMENGO', 'FORTALEZA', 'PALMEIRAS', 'BRAGANTINO', 'CORINTHIAS', 'INTERNACIONAL', 'FLUMINENSE',
     'CUIABÁ', 'ATHLETICO PR', 'ATLÉTICO GO', 'SÃO PAULO', 'AMERICA MG', 'CEARA SC', 'SANTOS', 'BAHIA', 'JUVENTUDE',
     'SPORT RECIFE', 'GRÊMIO', 'CHAPECOENSE')
print(f'Os cincos primeiros colocados são: {a[:5]}')
print(f'Os últimos 4 colocados são: {a[-4:]}')
print('Organizado de A-Z', sorted(a))
print(f"O time Chapecoense está na posição {(a.index('CHAPECOENSE'))+1}º")
