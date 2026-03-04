""" Desenvolva um programa que leia o nome, idade e sexo de QUATRO pessoas. No final do programa mostre:
A média de idade do grupo / Qual é o nome do homem mais velho  Quantas mulheres tem menos de 20 anos. """
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ' '
totmulher20 = 0
for p in range(1, 5):
    print('====== {}ª pessoa ======'.format(p))
    nome = str(input('Digite seu nome: ')).title().strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()
    somaidade += idade  # soma todas para depois tirar uma média
    if p == 1 and sexo in 'Mm': # Vai analisar se a 1ª pessoa é homem. Se for:
        maioridadehomem = idade # ele já fica na idade de mais velho (por ser o primeiro analisado e a se encaixar no if)
        nomevelho = nome # E o nome dele fica guardado para mais tarde.
    if sexo in 'Mm' and idade > maioridadehomem: # Vai analisar os demais para saber se eles se enquadram na condição:
        maioridadehomem = idade # Se aparecer outro homem, com idade maior que o anterior, ele passa a ter a maior idade
        nomevelho = nome # e é o nome deste de agora que vai ficar guardado para ser usado na resolução do exercício.
    if sexo in 'Ff' and idade <20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))
