# Faça um programa que leia um nome de usuário e a sua senha
# e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

user = input('Diga seu usuário: ')
senha = input('Diga sua senha: ')
while senha == user:
    print('Erro: usuário = senha')
    user = input('Diga seu usuário: ')
    senha = input('Diga sua senha: ')
print(f'Bem vindo, {user}.')
