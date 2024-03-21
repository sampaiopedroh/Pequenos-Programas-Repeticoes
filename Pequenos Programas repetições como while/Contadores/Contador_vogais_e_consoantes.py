# Programa para contar quantas vogais e consoantes da lista
qnt_letra = int(input('Quantas letras serão inseridas: '))
vezes = 0
vogais = 0
while vezes < qnt_letra:
    vezes += 1
    letras = input(f'Diga a {vezes}° letra: ')
    if letras == 'a' or letras == 'e' or letras == 'i' or letras == 'o' or letras == 'u':
        vogais += 1
print(f'A quantidades de vogais é {vogais} e de consoantes é {qnt_letra - vogais}.')
