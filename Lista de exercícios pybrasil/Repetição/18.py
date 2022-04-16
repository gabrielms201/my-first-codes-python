# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

n = int(input("Digite a quantidade de números: "))
menor = 0
maior = 0
soma = 0

while n <= 0 or n > 1000:
    n = int(input("Quantidade de números inválida!\nDigite a quantidade de números novamente: "))

for i in range(n):
    num = float(input("Digite um número: "))
    if i == 0:
        maior = menor = num
    else:
        if num > maior: 
            maior = num
        if num < menor:
            menor = num
    soma += num
print("\nMaior Número: %.2f\nMenor Número: %.2f\n\nSoma: %.2f" % (maior, menor, soma))