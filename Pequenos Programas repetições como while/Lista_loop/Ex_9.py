# Faça um programa que peça 10 números inteiros,
# calcule e mostre a quantidade de números pares
# e a quantidade de números ímpares.
qnt = 0
pares = 0
while qnt < 10:
    qnt += 1
    nums = int(input(f'Diga o {qnt}° número: '))
    if nums % 2 == 0:
        pares += 1
print(f'A quantidades de pares é: {pares}\n'
      f'A quantidade de ímpares é: {10 - pares}')