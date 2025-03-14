try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de erro.')
except ZeroDivisionError:
    print('Não é possível dividir por zero.')
except KeyboardInterrupt:
    print('O user preferiu não informar os dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Finalizado.')
