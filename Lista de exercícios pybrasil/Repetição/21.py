# Faça um programa que peça um número inteiro e determine se 
# ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input("Digite um número inteiro: "))

for i in range(2,num):
    if num % i == 0:
        print("O número não é primo")
        break
else:
    print("O número é primo")
    