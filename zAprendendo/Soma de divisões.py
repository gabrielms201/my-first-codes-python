# Escreva um programa que calcule e apresente a soma da seguinte série:
# 1 + 3/2 + 5/3 + 7/4 ... 99/50

soma = 0
a = 1
for i in range(1,51): 
    soma += a/i
    a += 2
print(soma)
