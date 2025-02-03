# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
# - quantidade de notas
# - a maior nota
# - a menor nota
# - a média da turma
# - a situação (opcional)
# Adicione também as docstrings da função

def notas(*notas, sit=False):
    """
    -> Informa os seguintes dados sobre as notas: QNT, MAIOR, MENOR, MÉDIA E SITUAÇÃO.
    :param notas: Escrever as notas separadas por vírgula.
    :param sit: Opcional, True se quiser mostrar.
    :return:
    """
    info = dict()
    info['qnt'] = len(notas)
    info['mai'] = max(notas)
    info['men'] = min(notas)
    info['med'] = sum(notas)/len(notas)
    if info['med'] >= 8:
        info['sitn'] = 'BOA'
    elif info['med'] < 4:
        info['sitn'] = 'RUIM'
    else:
        info['sitn'] = 'OK'

    print(f'{info['qnt']} nota(s) foram analisadas.\nMaior: {info['mai']}   Menor: {info['men']}   Média: {info['med']}')

    if sit:
        print(f'A situação acadêmica do estudante é {info['sitn']}.')

    print(info)

notas(9.0, 7, 2.5, 10, 1, 6, 5.5, 3.75, 12, 0.75, sit=True)