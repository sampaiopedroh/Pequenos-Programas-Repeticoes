# Faça um programa que leia 5 números e informe a soma e a média dos números.
qnt = int(input('Quantos números serão mediado ? '))
aux = qnt
num = 0
while qnt < 5:
    qnt += 1
    num += int(input('Diga um número: '))
print(f'{num / aux}')
