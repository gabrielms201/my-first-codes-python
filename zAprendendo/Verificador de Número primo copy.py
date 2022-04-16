"""
DESAFIO: Faça um código que indentifique se um número é ou não é um número primo

"""
"""
num = 427
if num > 1:
  for i in range(2, num):
    if num % i == 0:
      print("O numero não é primo")
      break
  else:
      print("O número é primo")
else:
    print("Especifique um valor maior que 1")

"""

num = int(input("Digite seu número:\n"))
for i in range(2, num):
  if num % i == 0:
    print("O numero não é primo")
    break
else:
    print("O número é primo")