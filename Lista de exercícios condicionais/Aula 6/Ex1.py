"""
Faça um programa que leia três números inteiros e encontra o menor deles. 
Sugestão: Sejam 3 números A, B e C. A ideia principal é: verificar se A é menor que B e C e se não for, 
verificar entre B e C 
"""

a = 423
b = 23 
c = 1

if a > b and a > c:
  if b > c:
    print(c,b,a)
  else:
    print(b,c,a)
elif b > a and b > c:
  if c > a:
    print(a,c,b)
  else:
    print(c,a,b)
elif c > a and c > b:
  if b > a:
    print(a,b,c)
  else:
    print(b,a,c)


