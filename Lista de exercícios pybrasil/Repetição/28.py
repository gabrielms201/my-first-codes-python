# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar 
# a quantidade de CDs e o valor para em cada um.

qnt = int(input("Digite a quantidade CDs: "))
soma = 0

for i in range(qnt): 
    preco = float(input("Digite o preço pago no dvd %d: " % (i+1)))
    soma += preco

media = soma/qnt
print("Foi pago em média R$: %.2f por dvd " % media)


