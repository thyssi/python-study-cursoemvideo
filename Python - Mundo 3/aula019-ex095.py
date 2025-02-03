# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
# aproveitamento de cada jogador.
l = 40
listaPlayers = list()
while True:
    infoPlayer = {'nome':str(input('Nome do jogador: ')).strip().capitalize(),
                   'partidas':int(input('Quantas partidas jogou? '))}

    listaGol = list()
    infoPlayer['gtot'] = 0

    for c in range (0, infoPlayer['partidas']):
            listaGol.append(int(input(f'Quantos gols {infoPlayer['nome']} fez na partida {c+1}? ')))
            infoPlayer['gtot'] += listaGol[c]
    infoPlayer['gols'] = listaGol

    listaPlayers.append(infoPlayer.copy())
    infoPlayer.clear()
    
    while True:
        continuar = str(input('Quer cadastrar outro jogador? [S/N] ')).lower().strip()
        print('-'*l)
        if continuar[0] in 'sn':
            break
    if continuar == 'n':
        break

print(f'{"#":<3}{"Player":<15}{"Gols":<15}{"Total":>7}')
print('-'*l)
for i, c in enumerate(listaPlayers):
    print(f'{(i+1):<3}{c['nome   ']:<15}{str(c['gols']):<15}{c['gtot']:>7}')
print('-'*l)

while True:
    while True:
        det = int(input('Insira o No. do Player para visualizar detalhes (999 finaliza): '))
        if 0 < det <= len(listaPlayers) or det == 999:
            break
    if det == 999:
        break
    print('=' * l)
    print(f'{"DETALHES PLAYER":^{l}}')
    print('=' * l)
    print(f'{listaPlayers[det - 1]['nome']}:')
    for i, v in enumerate(listaPlayers[det-1]['gols']):
        print(f'{f'No jogo {i+1} fez {v} gols.':^{l}}')
    print('=' * l)
print('FIM')