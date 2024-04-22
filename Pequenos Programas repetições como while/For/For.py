# for char in 'pedro':
#     print(char)

# for i in range(1, 10, 1): #start, end, step
#     print(i)

# Soma de 1 à 100
# aux = 0
# for i in range(1, 101):
#     aux += i
# print(aux)

# 3 tentativas de senha
# user = input('Diga seu usuário: ')
# senha_certa = '1234'
# senha = input('Diga sua senha: ')
# for i in range(1, 2):
#     if senha == senha_certa:
#         break
#     senha = input(f'Senha incorreta, mais {3 - i} tentativas: ')
# print(f'Bem vindo {user}')

# Soma de 10 n° aleatórios
# qnt = int(input('Diga quantos números serão somados: '))
# num = 0
# for i in range(1, (qnt + 1)):
#     num += int(input(f'Diga o {i}° número: '))
# print(f'A média da soma dos {qnt} números é: {num / qnt}')

# Todas as tabuádas
# for tab in range(1, 11):
#     for num in range(1, 11):
#         print(f'{num} x {tab} = {num * tab}')

# Fibo
# tam = int(input('Diga o tamanho da sequência: '))
# a = 0
# b = 0
# for i in range(1, (tam + 1)):
#     c = a + b
#     if c == 0:
#         print(1)
#         a += 1
#     else:
#         print(c)
#         b = a
#         a = c
