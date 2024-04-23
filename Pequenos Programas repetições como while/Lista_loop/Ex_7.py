# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de 1 a 10.

# Básico:
# qnt = 0
# num = int(input('Diga um número: '))
# while qnt < 10:
#     qnt += 1
#     cal = num * qnt
#     print(f'{num} X {qnt} = {cal}')

# Todas
tab = 1
while tab <= 10:
    num = 1
    while num <= 10:
        print(f'{tab} X {num} = {num * tab}')
        num += 1
    tab += 1
