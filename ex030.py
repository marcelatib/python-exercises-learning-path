# Crie um programa que leia um número INTEIRO e mostre na tela se ele é par ou se é ímpar.
num = int(input('Digite um número inteiro qualquer: '))
if num % 2 == 0:
    print('O número {} é par!'.format(num))
else:
    print('O número {} é ímpar!'.format(num))