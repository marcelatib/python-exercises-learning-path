""" Escreva um programa que leia DOIS NÚMEROS INTEIROS e compare-os, mostrando na tela uma mensagem:
0 - o primeiro valor é MAIOR / 1 - o segundo valor é maior / 2 - Não existe valor maior, os dois são iguais. """
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
print('Vou agora fazer a comparação entre {} e {} ...'.format(n1, n2))
if n1 > n2:
    print('O primeiro valor é maior!')
elif n2 >n1:
    print('O segundo valor é maior!')
else:
    print('Não existe valor maior. Os dois são iguais.')
