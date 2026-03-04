# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m². Quantos litros de tinta irá precisar para pintar a parede toda?
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parece tem a dimensão de {} x {} e a sua área é de {:.2f}m².'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {:.2f} litros de tinta.'.format(tinta))