"""'
Faça um programa que leia 5 números e informe a soma e a média dos números.
"""

soma = 0
qnt = 5

for i in range(qnt):
    num = float(input("Digite um número: "))
    soma += num

media = soma/qnt
print("\nSoma dos números: %.2f\nMédia dos números: %.2f" % (soma, media))
