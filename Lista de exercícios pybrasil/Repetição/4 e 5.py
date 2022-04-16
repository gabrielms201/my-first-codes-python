"""
Supondo que a população de um país A seja da ordem de 80000 (80mil) habitantes com uma
taxa anual de crescimento de 3% e que a população de B seja 200000 (200mil) habitantes com uma
taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos 
necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
"""

while True:
    a = float(input("Digite o número de habitantes de A: "))
    b = float(input("Digite o número de habitantes de B: "))
    crescimento_a = float(input("Digite a taxa de crescimento de habitantes de A: "))/100
    crescimento_b = float(input("Digite a taxa de crescimento de habitantes de B: "))/100
    anos = 0
    while a < b:
        a += (a*crescimento_a)
        b += (b*crescimento_b)
        anos += 1

    print("Vão demorar %d anos para que a população de A ultrapasse ou iguale a população de B\n" % anos)
    continuar = str.lower(input("Deseja continuar? (S/N)"))
    if continuar == "s":
        True
    elif continuar == "n":
        break
    else:
        continuar = str.lower(input("Deseja continuar? (S/N)"))





