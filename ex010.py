# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere U$$ = 3,27
reais = float(input('Quantos dinheiro você tem em R$? '))
dolar = reais / 5.75
print('Com R$ {} você pode comprar $ {:.2f}. '.format(reais, dolar))
