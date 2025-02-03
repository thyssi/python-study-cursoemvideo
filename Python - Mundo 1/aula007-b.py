n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
sm = n1+n2
sb = n1-n2
m = n1*n2
d = n1/n2
e = n1**n2
di = n1//n2
dr = n1%n2

print (f'A soma é {sm}, \n a subtração é {sb}, o produto é {m}, a divisão é {d:.2f} e o expoente é {e}', end='. ')
print (f'A divisão resulta em {di} inteiros e {dr} de resto.')
