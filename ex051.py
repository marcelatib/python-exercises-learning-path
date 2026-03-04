""" Desenvolva um programa que leia o PRIMEIRO TERMO e a RAZÃO de uma Progressão Aritmética. No final, mostre os 10 primeiros
termos dessa progressão. """
print('=' * 30)
print('         10 TERMOS DE UMA PA')
print('=' * 30)
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo, razao):
    print('{}'.format(c), end=' ➞ ')
print('ACABOU')
