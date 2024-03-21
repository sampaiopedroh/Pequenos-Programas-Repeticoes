# Programa para realizar a soma dos n˚ colocados na lista
qnt_num = 0
soma = 0
qnt_soma = int(input('Quantos números serão somados: '))
while qnt_num < qnt_soma:
    qnt_num += 1
    num = int(input(f'Digite {qnt_num}° número: '))
    soma += num
print(f'A soma dos {qnt_soma} números é igual a: {soma}')
