# Programa para formar uma frase
qnt_pala = int(input('Quantas palavras tem sua frase ? '))
vezes = 0
frase = ''
while vezes < qnt_pala:
    vezes += 1
    palavras = input(f'Digite a {vezes}° palavra: ')
    frase += palavras + ' '
print(f'Sua frase é:\n'
      f'{frase}')
