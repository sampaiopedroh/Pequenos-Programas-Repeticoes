#  Faça um programa que calcule o fatorial de um número inteiro
#  fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
num = int(input('Diga o número: '))
fat = num
aux = num
# while num > 1:
#     num -= 1
#     fat *= num
# print(f'O fatorial de {aux} é: {fat}')

fat_string = f'{num}'
while num > 1:
    num -= 1
    fat *= num
    fat_string += f'.{num}'

print(f'A sequência fatorial de {aux} é: {fat_string} = {fat}')