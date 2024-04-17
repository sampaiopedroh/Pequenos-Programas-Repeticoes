# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input('Diga seu nome: ')
qnt_letras = len(nome)
while qnt_letras <= 2:
    nome = input('Diga um nome válido: ')
    qnt_letras = len(nome)

idade = int(input('Diga sua idade: '))
while not 0 < idade <= 150:
    idade = int(input('Diga uma idade válida: '))

sal = int(input('Diga seu salário: '))
while sal <= 0:
    sal = int(input('Diga um salário válido: '))

sexo = input('Diga seu sexo ("f" ou "m"): ')
while True:
    if sexo == 'f' or sexo == 'm':
        break
    sexo = input('Digite um sexo válido: ')

est_civil = input('Diga seu estado civil ("s", "c", "v" ou "d"): ')
while True:
    if est_civil == 's' or est_civil == 'c' or est_civil == 'v' or est_civil == 'd':
        break
    est_civil = input('Diga um estado civil válido: ')

print(f'Seu nome: {nome}\n'
      f'Sua idade: {idade}\n'
      f'Seu salário: {sal}\n'
      f'Seu sexo: {sexo}\n'
      f'Seu estado civil: {est_civil}')

