""" Faça um programa que CALCULE A SOMA entre todos os números ÍMPARES (o ex não quer saber quais são) que são MULTIPLOS DE 3
e que se encontram no intervalo de 1 até 500. """
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        s+= c
print('A soma entre todos os {} números ímpares que são múltiplos de três entre 1 e 500 é \033[1;35m{}\033[m.'.format(cont, s))
