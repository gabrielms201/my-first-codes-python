"""
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
"""
pares = 0
impares = 0 

for i in range(10):
    num = int(input("Digite um número: "))
    if num % 2 == 0: pares +=1
    else: impares +=1

print("Quantidade de números pares:%d\nQuantidade de números ímpares:%d" % (pares, impares))

