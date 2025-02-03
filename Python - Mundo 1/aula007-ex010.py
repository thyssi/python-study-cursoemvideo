# Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dólares ela pode comprar.
title = ' MINHA CARTEIRA'
print(f'\nInforme a quantidade de notas e moedas: \n\n{title:=>25}')
n200 = int(input('R$200 x '))
n100 = int(input('R$100 x '))
n50 = int(input('R$50 x '))
n20 = int(input('R$20 x '))
n10 = int(input('R$10 x '))
n5 = int(input('R$5 x '))
n2 = int(input('R$2 x '))
m1 = int(input('R$1 x '))
m50 = int(input('R$0.50 x '))
m25 = int(input('R$0.25 x '))
m10 = int(input('R$0.10 x '))
m5 = int(input('R$0.05 x '))

tn200 = float(n200*200)
tn100 = float(n100*100)
tn50 = float(n50*50)
tn20 = float(n20*25)
tn10 = float(n10*10)
tn5 = float(n5*5)
tn2 = float(n2*2)
tm1 = float(m1*1)
tm50 = float(m50*0.5)
tm25 = float(m25*0.25)
tm5 = float(m5*0.05)

title2 = f' TOTAL: R$ {(tn200+tn100+tn50+tn20+tn10+tn5+tn2+tm1+tm50+tm25+tm5):.2f}'
print(f'{title2:=>25}')
title3 = f' USD {((tn200+tn100+tn50+tn20+tn10+tn5+tn2+tm1+tm50+tm25+tm5)/6.09):.2f}'
print(f'{title3:=>25}')

