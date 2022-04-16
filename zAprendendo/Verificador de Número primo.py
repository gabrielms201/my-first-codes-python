"""
DESAFIO: Faça um código que indentifique se um número é ou não é um número primo

"""

inputNum = int(input("Digite o seu número: "))
if inputNum > 1:
  for i in range (2, inputNum):
    if (inputNum % i) == 0:
      print("O número ",inputNum,"não é primo")
      break
  else:
      print("O número ", inputNum, " é primo")
else: 
  print("O número ", inputNum, "não é primo")     


