# Faça um programa que mostre os n termos da Série a seguir:
#Imprima no final a soma da série

soma = 0
a = 1
for i in range(1,51): 
    soma += i/a
    print("%d/%d" % (i,a), end = "")
    print(" = " if i == 50 else " + ", end = "")
    a += 2
print(soma)
print("\nSoma: %.2f"%soma)
