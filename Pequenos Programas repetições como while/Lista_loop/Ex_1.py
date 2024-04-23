# Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e
# continue pedindo até que o usuário informe um valor válido.

# Normal:
# nota = int(input('Diga sua nota: '))
# while not (0 < nota <= 10):
#     nota = int(input('Diga uma nota válida: '))
# print(f'Sua nota é: {nota}')

# Com .isnumeric()
nota = input('Diga sua uma nota: ')
while not nota.isnumeric():
    nota = input('Diga uma nota válida: ')
print('Nota válida')
