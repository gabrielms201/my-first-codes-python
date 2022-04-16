# Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
# Exemplo:
#   12376489
#   => 98467321

n = int(input("Digite o número: "))
valor = str(n)
b = len(valor)-1
for e in valor:
    print(valor[b],end = "")
    b-=1


# Também é possível utilizar: 
# print str(input("Digite o número: "))[::-1]
