# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. 
# A entrada de dados deverá terminar quando for lido um número negativo.

n = float(input("Digite um número: "))
while n >= 0:
    if n >= 0 and n <= 25:
        print("Está no intervalo [0-25]")
        n = float(input("Digite um número: "))
    elif n >= 26 and n <= 50:
        print("Está no intervalo [26-50]")
        n = float(input("Digite um número: "))
    elif n >= 51 and n <= 75:
        print("Está no intervalo [51-75]")
        n = float(input("Digite um número: "))
    elif n>= 71 and n <= 100:
        print("Está no intervalo [76-100]")
        n = float(input("Digite um número: "))
    else:
        print("Está no intervalo [101-ထ ]")
        n = float(input("Digite um número: "))