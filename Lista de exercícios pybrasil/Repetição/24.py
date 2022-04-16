# Faça um programa que calcule o mostre a média aritmética de N notas

n = int(input("Digite a quantidade de notas que deseja calcular: "))
qtd = 0
soma = 0

while n > 0:
    nota = float(input("Digite a nota: "))
    soma += nota
    qtd += 1
    n -= 1
media = soma/qtd

print("Média = %.2f" % media)
