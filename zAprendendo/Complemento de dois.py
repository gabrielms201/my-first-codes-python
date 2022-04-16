import os
def conversor():
  num = int(input("Digite o seu número em complemento de 2:\n"), 2)
  if str(num)[0] == "1":
    funNot = (~num & 255)
    inc = ~ funNot
    print(f"O número é igual à: [{bin(inc)}], ou em decimal: [{inc}]")
  else:
    print(f"O número é igual à: [{bin(num)}], ou em decimal: [{num}]")
def saida():
  sair = input("Digite s para sair, ou aperte enter para continuar\n")
  if sair == "s" or sair == "S":
    os.system("cls" if os.name == "nt" else "clear")
    return True
  else:
    return False
while True:
  conversor()
  if saida() == True:
    break




  
