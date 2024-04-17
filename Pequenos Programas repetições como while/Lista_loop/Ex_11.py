# Faça um programa que peça um número inteiro e
# determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.
num = int(input('Diga um número: '))
i = 2
# Testando com todos
'''while i < num:
    div = num % i
    print(f'{num} % {i} = {div}')
    if div == 0:
        print(f'{num} não é primo')
        break
    elif i == -1:
        print(f'{num} é primo')
    i += 1'''

# Testando com metade
'''while True:
    div = num % i
    if div == 0:
        print(f'{num} não é primo')
        break
    elif i >= num/2:
        print(f'{num} é primo')
        break
    i += 1'''

# Testando até a raiz quadrada
while True:
    div = num % i
    if div == 0:
        print(f'{num} não é primo')
        break
    elif i >= num**1/2:
        print(f'{num} é primo')
        break
    i += 1