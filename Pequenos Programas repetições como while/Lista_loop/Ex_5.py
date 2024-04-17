# Faça um programa que receba dois números inteiros
# e gere os números inteiros que estão no intervalo compreendido por eles.

qnt = 0
num = 0
while qnt < 2:
    qnt += 1
    aux = num
    num = int(input('Diga um número: '))
    cal = num - aux
print((cal ** 2) ** (1/2))
