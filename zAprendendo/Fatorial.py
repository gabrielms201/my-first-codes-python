#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
#num = 5
#fac = 5 * (5-1) * (5-2) * (5-3) * (5-4)
#print(fac) -> Output 120

num = float(input("Digite o número: "))
num_inicial = num
fato = 1

while num > 1:
    fato = num * fato
    num -= 1 
print("%.2f! = %.f" % (num_inicial, fato))

