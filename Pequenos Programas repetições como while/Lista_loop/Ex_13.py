# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# 1. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# 2. Em 2020 recebeu aumento de 1,5% sobre seu salário inicial;
# 3. A partir de 2021 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
sal = int(input('Diga o valor do seu primeiro salário: '))
atual = int(input('Em que ano estamos (em números): '))
partida = 1995
taxa = 0.015
while partida < atual:
    sal *= 1+taxa
    taxa *= 2
    partida += 1
print(f'Seu salário em {atual} é de R${sal}')