# Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. 
# Um número primo é aquele que é divisível apenas por um e por ele mesmo. 
# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

num = int(input("Digite um número: "))

for i in range(2, num):
    if num % i == 0:
        marcador = True
        break

if marcador:
    print("O número não é primo")
else:
    print("O número é primo")







