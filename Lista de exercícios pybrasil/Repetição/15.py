# "A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.


n = int(input("Digite o valor de n: "))
f1 = 1
f2 = 0

for i in range (n):
     f3 = f1+f2
     f1 = f2
     f2 = f3
     print(f3)