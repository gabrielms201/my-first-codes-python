# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120

num = 5
fato = 1
print("%d!=" % num, end = " ")
for i in range(0, num):
    fato *= num
    print(num, end = "")
    print("*", end = "" if num > 1 else " = ")
    num -= 1
print(fato)