# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programador vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

info = {'nome':str(input('Nome do jogador: ')).capitalize(),
        'partidas':int(input('Quantas partidas jogou? '))}
n = info['partidas']
lista = list()
l = 40
for c in range (0, n):
        lista.append(int(input(f'Quantos gols {info['nome']} fez na partida {c+1}? ')))
        info['gols'] = lista
info['gtot'] = sum(info['gols'])

print('='*l)
print(info)
print('='*l)
print(f'{info['nome']} jogou {info['partidas']} partida(s) e fez {info['gtot']} gol(s) ao total.')
print('='*l)
for c in range (0, n):
        print(f'==> Na partida {c+1}, {info['nome']} fez {lista[c]} gol(s).')
print('='*l)