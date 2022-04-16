# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
# Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = 0 

print("Números no intervalo entre %d e %d: " % (num1,num2))
for i in range(num1+1,num2):
    print(i, end = "")
    print(", " if i < num2-1 else ". ", end = "")
    soma += i



print("\nSoma do intervalo: %d" % soma)