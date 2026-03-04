# Crie um algorítmo que leia um número e mostre o seu dobro, triplo e a raíz quadrada.
n = float(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
r = n ** (1/2)
print('O número digitado foi {:.0f}. \nO dobro dele é {:.0f},\nO triplo é {:.0f},\nA raíz quadrada é {:.0f}.'.format(n, dobro, triplo, r))
