# Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$ 0,50 por KM
# para viagens de ATÉ 200 KM e R$ 0,45 para viagens mais longas.
viagemkm = float(input('Digite os quilômetros distância daqui até o destino escolhido: '))
if viagemkm <= 200:
    valor = viagemkm * 0.5
    print('Para {} quilômetros, o custo da passagem são R$ {}.'.format(viagemkm, valor))
else:
    valor = viagemkm * 0.45
    print('Para {} quilômetros, o valor da passagem são de R$ {}.'.format(viagemkm, valor))