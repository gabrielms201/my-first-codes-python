"""
Faça um programa que leia 5 números e informe o maior número.
"""

maior = 0
for i in range(5):
    num = float(input("Digite o seu número: "))
    if num > maior:
        maior = num
print("Maior número: %f" % maior)