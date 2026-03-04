""" Crie um programa que faça o computar jogar Jokenpô com você. Ver no google as regras do pedra, papel, tesoura. """
import random
import time
opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA''')
pc = random.randint (0,2)
jogador = int(input('Qual é a sua jogada? '))
print('... VERIFICANDO O RESULTADO ...')
time.sleep(2) #Pausa de 2 segundos para ter suspense
if jogador == 0 and pc == 0:
    print('Empatou')
elif jogador == 0 and pc == 1:
    print('Computador Venceu :( ')
elif jogador == 0 and pc == 2:
    print('\033[1;31mMarcela Venceu, uhuuu!\033[m')
elif jogador == 1 and pc == 1:
    print('Empatou')
elif jogador == 1 and pc == 0:
    print('\033[1;31mMarcela Venceu, uhuuul\033[m')
elif jogador == 1 and pc == 2:
    print('Computador Venceu :( ')
elif jogador == 2 and pc == 2:
    print('Empatou')
elif jogador == 2 and pc == 0:
    print('Computador Venceu :( ')
elif jogador == 2 and pc == 1:
    print('\033[1;31mMarcela Venceu, uhuuul\033[m')
else:
    print('\033[1;31mOPÇÃO INVÁLIDA.\033[m Tente novamente.')
if 0 <= jogador <= 2:
    print(f'O computador jogou {opcoes[pc]}.')
    print(f'Marcela jogou {opcoes[jogador]}.')