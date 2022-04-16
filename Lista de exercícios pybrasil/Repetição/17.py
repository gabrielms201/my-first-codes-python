# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

num = int(input("Digite um número inteiro: "))
num_inicial = num
fat = 1

for i in range(num):
    fat = num * fat
    num -= 1

print("%d! = %d" % (num_inicial, fat))