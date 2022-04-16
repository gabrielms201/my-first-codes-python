# Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

num = 100
for i in range(1, num):
    for j in range(2, i):
        if i%j == 0:
            primo = False
            break
    else: print(i)