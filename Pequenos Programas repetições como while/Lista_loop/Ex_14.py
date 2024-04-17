# Faça um programa que leia uma quantidade indeterminada de números positivos
# e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
# A entrada de dados deverá terminar quando for lido um número negativo.
pri = 0
seg = 0
ter = 0
qua = 0
i = 0
while True:
    num = input(f"Diga o {i+1}° número (para sair, digite '-'): ")
#   'if num > 0:' ou
    if '-' in num:
        print(f'Há {pri} números no primeiro intervalo\n'
              f'Há {seg} números no segundo intervalo\n'
              f'Há {ter} números no terceiro intervalo\n'
              f'Há {qua} números no quarto intervalo')
        break
    if not num.isnumeric():
        print('Deve ser um número !')
        continue
    num = int(num)
    if num <= 25:
        pri += 1
    elif num <= 50:
        seg += 1
    elif num <= 75:
        ter += 1
    elif num <= 100:
        qua += 1
    i += 1