# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de 1 a 10.

# Básico:
# qnt = 0
# num = int(input('Diga um número: '))
# while qnt < 10:
#     qnt += 1
#     cal = num * qnt
#     print(f'{num} X {qnt} = {cal}')

# Todas
qnt = 0
num = 0
while qnt <= 10:
    qnt += 1
    qntx = 0
    while num <= 10:
        qntx += 1
        cal = num * qntx
        print(f'{num} X {qntx} = {cal}')
        if qntx == 10:
            break
    num += 1
