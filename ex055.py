""" Faça um programa que leia o peso de CINCO pessoas. No final, mostre qual foi o maior e o menor peso lidos. """
maior_peso = 0
menor_peso = 0
for p in range(1, 6):
    peso = float(input('Digite {}º peso em Kg: '.format(i)))
    if p == 1: # o peso está avaliando a primeira pessoa informada
        maior_peso = peso # se só avaliou a primeira pessoa, o maior peso é dela
        menor_peso = peso # se só avaliou a primeira pessoa, o menor peso é dela
    else: #aqui ele começa a avaliar da segunda pessoa para frente, comparando se o maior e menor peso contibuam os anteriores
        if peso < menor_peso: # Se o peso avaliado na rodada for menor do que o menor peso registrado:
            menor_peso = peso # ELE passa a ser o menor peso agora.
        if peso > maior_peso: # Se o peso avaliado na rodada dor maior do que o maior peso registrado até agora,
            maior_peso = peso # ELE passa a ser o maior peso agora.
# Lembrando que ele vai avaliar 5 vezes, por que o range é de 1 a 6. E ele vai ficar os os maior e o menor entre os 5 inputados pelo usuário.
print('O menor peso foi de {:.0f} Kgs.'.format(menor_peso))
print('O maior peso foi de {:.0f} Kgs.'.format(maior_peso))
