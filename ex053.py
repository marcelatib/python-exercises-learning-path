""" Crie um programa que leia uma frase qualquer e diga SE ELA É um PALÍNDROMO, desconsiderando os espaços. (frases que se lê de
frente para trás ou de trás para frente e que é a mesma coisa. Sem acento, mas com espaços e o programa vai desconsiderar estes espaços.
 Tipo: 'A mala nada na lama' , 'O lobo ama bolo', 'A torre da derrota' etc.   """
frase = str(input('Digite a frase a ser analisada: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso+= junto [letra]
print('O inverso de {} é {}....'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada NÃO é um palíndromo!')
