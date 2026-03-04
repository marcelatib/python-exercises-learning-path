#Escreva um programa que faça o computador "pensar" em um número entre 0 e 5, e peça para o usuário tentar descobrir qual foi
# o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
import time
print('Tente descobrir em que número eu pensei entre 0 e 5...')
numero_computador = random.randint(0, 5) #o cumputador "pensa" em um número
chute_usuario = int(input('Em que número eu acabei de pensar? '))
print('PROCESSANDO...')
time.sleep(2) #Pausa de 2 segundos para ter suspense
if chute_usuario == numero_computador:
    print('PARABÉNS! VOCÊ ACERTOU!!!!')
else:
    print('What a shame! Você errou! \nEu pensei no número {}.'.format(numero_computador))
