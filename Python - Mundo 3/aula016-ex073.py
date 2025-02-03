# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
# colocação. Depois mostre:
# a) apenas os 5 primeiros colocados.
# b) os últimos 4 colocados da tabela
# c) uma lista com os times em ordem alfabética
# d) em que posição na tabela está o time da Corinthians.

times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional',
         'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco', 'Vitória',
         'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude', 'Bragatino',
         'Atlético-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá')

print(f'''
Os cinco primeiros colocados são:
1. {times[0]}
2. {times[1]}
3. {times[2]}
4. {times[3]}
5. {times[4]}

Os últimos 4 colocados são:
20. {times[-1]}
19. {times[-2]}
18. {times[-3]}
17. {times[-4]}

Os times em ordem alfabética fica: 
{sorted(times)}

O time do Corinthians está na {(times.index('Corinthians')+1)}° posição da tabela.''')