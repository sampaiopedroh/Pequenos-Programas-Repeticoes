# Em uma eleição presidencial existem quatro candidatos.
# Os votos são informados por meio de código.
# Os códigos utilizados são:
# 1 , 2, 3, 4  - Votos para os respectivos candidatos
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco

# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos.
# Para finalizar o conjunto de votos tem-se o valor zero.
a = 0
b = 0
c = 0
d = 0
n = 0
br = 0
qnt = 0
print('Opções de voto:\n'
      '1 - Ana\n'
      '2 - Bia\n'
      '3 - Caio\n'
      '4 - Davi\n'
      '5 - Nulo\n'
      '6 - Branco\n'
      '7 - Sair')
votos_poss = ['1', '2', '3', '4', '5', '6', '7']
while True:
    voto = input('Diga seu voto: ')
    if voto == '7':
        break
    while voto not in votos_poss:
        print('Digite uma opção válida')
        voto = input('Diga seu voto: ')
    if voto == '1':
        a += 1
    elif voto == '2':
        b += 1
    elif voto == '3':
        c += 1
    elif voto == '4':
        d += 1
    elif voto == '5':
        n += 1
    else:
        br += 1
    qnt += 1
print(f'Ana recebeu: {a} votos\n'
      f'Bia recebeu: {b} votos\n'
      f'Caio recebeu: {c} votos\n'
      f'Davi recebeu: {d} votos\n'
      f'Há {n} votos nulos ({(n/qnt)*100:.2f}%)\n'
      f'Há {br} votos brancos ({(br/qnt)*100:.2f}%)')