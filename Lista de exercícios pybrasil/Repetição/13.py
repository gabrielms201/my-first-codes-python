# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
# Não utilize a função de potência da linguagem.

base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))
num = 1

for i in range(expoente):
    num = num * base


print(num)




