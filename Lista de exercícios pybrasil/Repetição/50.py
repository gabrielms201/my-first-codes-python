# Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.
n = int(input("Digite o valor desejado de N: "))
soma = 0
for i in range(1, n+1):
    soma += (1/i)
print("H = %s "%soma)