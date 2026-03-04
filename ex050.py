""" Desenvolva um programa que leia seis números inteiros e MOSTRE A SOMA apenas daqueles que forem PARES.
Se o valor digitado for ímpar, desconsidere-o. """
soma= 0 # precisa ser iniciada antes do laço
cont = 0 #colocar o contador de quantos números foram
for c in range(1, 7):
    num = int(input('{}º número : '.format(c)))
    if num % 2 == 0:
        soma += num # acumula os pares
        cont += 1
print('Você informou {} números pares e a soma entre eles é {}'.format(cont, soma))
