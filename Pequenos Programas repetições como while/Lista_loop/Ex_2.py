# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input('Diga seu nome: ')
qnt_letras = len(nome)
while qnt_letras < 3:
    nome = input('Diga um nome válido: ')
    qnt_letras = len(nome)

idade = input('Diga sua idade: ')
while not idade.isnumeric() or int(idade) > 150:
    idade = input('Diga uma idade válida: ')

sal = input('Diga seu salário (sem os centavos): ')
while not sal.isnumeric() or int(sal) < 0:
    sal = input('Diga um salário válido: ')

sexo = input('Diga seu sexo:\n'
             'm - masculino\n'
             'f - feminino')
while sexo != 'm' or sexo != 'm':
    sexo = input('Diga um sexo válido')

est_civil = input('Informe seu estado civil:\n'
                  's - solteiro(a)\n'
                  'c - casado(a)\n'
                  'v - viúvo(a)\n'
                  'd - divorciado(a)')
est_possiveis = ['s', 'c', 'v', 'd']
while est_civil != est_possiveis:
    est_civil = input('Diga um estado civil válido: ')
if est_civil == 's':
    est_civil = 'Solteiro(a)'
elif est_civil == 'c':
    est_civil = 'Casado(a)'
elif est_civil == 'v':
    est_civil = 'Viúvo(a)'
else:
    est_civil = 'Divorsiado(a)'

print(f'Seu nome: {nome}\n'
      f'Sua idade: {idade} anos\n'
      f'Seu salário: R${sal}\n'
      f'Seu sexo: {sexo}\n'
      f'Seu estado civil: {est_civil}')

