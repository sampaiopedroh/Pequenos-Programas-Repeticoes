# A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.
tam = int(input('Digite qual a quantidade da série de Fibonacci: '))
qnt = 0
a = 0
b = 0
c = 0
while qnt < tam:
    c = a + b
    b = a
    a = c
    if a == 0:
        a += 1
        c = 1
    qnt += 1
    print(c)
