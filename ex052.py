""" Faça um programa que leia um NÚMERO INTEIRO e diga se ele é ou não um número PRIMO. Só / por 1 e ele mesmo"""
tot = 0
num = int(input('Digite um número natural inteiro: '))
for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
if tot == 2:
    print('O número {} \033[1;32mé primo\033[m!'.format(num))
else:
    print('O número {} \033[1;36mnão é primo\033[m!'.format(num))