lista = list()
def linha_separacao(n):
    print('—'*n)
def titulo(t, n=30):
    print(f'{t.upper():^{n}}')
def opcao(n, t):
    print(f'\033[33m{n} — \033[34m{t.capitalize()}\033[m')
def cadastrar_dados(n, i):
    global lista
    info = dict()
    info['nome'], info['idade'] = n, i
    lista.append(info.copy())
def ver_dados(l):
    for c in lista:
        nome = c['nome']
        idade = f'{c['idade']}{' anos'}'
        blank = ' ' * (l - len(nome) - len(idade))
        print(f'{nome}{blank}{idade}')