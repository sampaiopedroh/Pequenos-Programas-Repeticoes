# Programa para contar números pares e ímpares
"""pares = 0
num = int(input('Digite um dividendo: '))
if num % 2 == 0:
    pares += 1
num = int(input('Digite um dividendo: '))
if num % 2 == 0:
    pares += 1
num = int(input('Digite um dividendo: '))
if num % 2 == 0:
    pares += 1
num = int(input('Digite um dividendo: '))
if num % 2 == 0:
    pares += 1
num = int(input('Digite um dividendo: '))
if num % 2 == 0:
    pares += 1
impares = 5 - pares
print(f'Há {pares} números pares e {impares} números ímpares')"""

# Com while
repet = 0
pares = 0
while repet < 5:
    num = int(input("Diga um número: "))
    if num % 2 == 0:
        pares += 1
    repet += 1
impares = 5 - pares
print(f'Há {pares} números pares e {impares} números ímpares')
