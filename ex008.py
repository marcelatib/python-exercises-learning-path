#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Digite um valor em metros: '))
cent = m*100
milim = m * 1000
print('Você digitou {} metros. Isso é equivalente a {} centímentros, e a {} milímetros.'.format(m, cent, milim))
