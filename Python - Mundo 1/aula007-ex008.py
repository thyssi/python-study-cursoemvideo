# Desenvolva em programa que leia em metros e exiba convertido em cm e mm.
m = float(input('Medida em metros: '))
cm = m*100
mm = m*1000
print(f'Equivale a:\n{cm:.2f} cm\n{m:.2f} m\n{mm:.2f} mm')