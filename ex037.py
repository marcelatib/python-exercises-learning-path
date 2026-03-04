""" Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 para BINÁRIO / 2 para OCTAL / 3 para HEXADECIMAL"""
num = int(input('Digite um número inteiro: '))
opc = int(input('''Escolha uma das opções de base de conversão abaixo: '))
[1] - Binário
[2] - Octal
[3] - Hexadecimal 
Digite aqui a sua escolha: '''))
if opc == 1:
    print('Na conversão em Binário, o número {} corresponde a {}.'.format(num, bin(num)[2:]))
elif opc == 2:
    print('Na conversão em Octal, o número {} corresponde a {}.'.format(num, oct(num)[2:]))
elif opc == 3:
    print('Na conversão em Hexadecimal, o número {} corresponde a {}.'.format(num, hex(num)[2:]))
else:
    print('Opção {} inválida. Escolha apena entre 1, 2 ou 3.'.format(opc))
