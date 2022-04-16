# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

num = int(input("Digite um número inteiro: "))
verificador = 0

for i in range(2,num):
    if num % i == 0:
        verificador += 1
        if verificador == 1:
            print("O número não é primo, pois ele é divisível por:\n%d" % i,end = "")
        else: print(i)
    if i == num-1:
        print("\nAlém de ser divisível por 1 e por %d" % num)
    
if verificador == 0:
    print("O número é primo")