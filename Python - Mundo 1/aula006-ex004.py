n = input('Variável a ser analisada: ')
print (f'Tipo:', type(n))
print (f'É alfabético: {n.isalpha()}')
print (f'É numérico: {n.isnumeric()}')
print (f'É alfanumérico: {n.isalnum()}')
print (f'Só tem espaços: {n.isspace()}')
print (f'Está em maiúsculo: {n.isupper()}')
print (f'Está em minúsculo: {n.islower()}')
print (f'Está capitalizada: {n.istitle()}')