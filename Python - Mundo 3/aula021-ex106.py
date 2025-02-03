# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
# OBS: Use cores.
def syshelp():
    while True:
        #cores
        cor_title = '\033[97;42m'
        cor_acessando = '\033[97;44m'
        cor_funcao = '\033[30;107m'
        cor_fim = '\033[m'

        #title
        title = 'SISTEMA DE AJUDA PyHelp'
        l = len(title) + 10
        print(cor_title+'~'*l)
        print(f'{title:^{l}}')
        print(f'~'*l)

        funcao = input(cor_fim+'Função ou biblioteca: ').strip().lower()
        if funcao == 'FIM':
            break

        #acessando
        title = f"Acessando o manual do comando '{funcao}'"
        l = len(title) + 10
        print(cor_acessando+'~'*l)
        print(f'{title:^{l}}')
        print(f'~'*l)

        #help
        print(cor_funcao, end='')
        help(funcao)

syshelp()
