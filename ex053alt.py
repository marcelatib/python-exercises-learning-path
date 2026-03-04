frase = input('Digite a frase a ser analisada: ').replace(' ', '').lower()
if frase == frase[::-1]:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo.')
