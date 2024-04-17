# Faça um programa que calcule o mostre a média aritmética de N notas.
qnt = int(input('Quantas notas serão calculadas ? '))
aux = qnt
notas = 0
while qnt > 0:
    nota = int(input(f'Diga uma nota: '))
    notas += nota
    qnt -= 1
media = (notas / aux)
print(f'A médias das {aux} notas é: {media}')