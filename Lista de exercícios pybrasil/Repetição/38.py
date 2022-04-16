# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
# Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

salario = int(input("Digite o salário inicial em 1995: "))
#Ano de 1996
aumento = 1.5/100
salario = salario + (salario*aumento)
aumento = 2 * aumento

ano = int(input("Digite o ano que deseja visualizar o salário: "))
tempo = (ano - 1997)+1

for i in range(tempo):
    salario = salario + (salario*aumento)
    aumento = aumento * 2
print("Salário em %d = %.2f" % (ano, salario))