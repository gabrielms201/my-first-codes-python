"""
Calcular programa para resolver eq de segundo grau
Valores de teste bons: a = 1, b= -1, c=-12
Resultados esperados: 4 e -3
"""
import math
while True:
  valora = float(input("Qual o valor de a?\n"))
  valorb = float(input("Qual o valor de b?\n"))
  valorc = float(input("Qual o valor de c?\n"))
  delta = valorb**2 - (4*valora*valorc)

  if delta < 0:
    print("Delta é negativo, logo não podemos dizer uma solução real para a equação, tendo o valor de delta como: {0}".format(delta))
  elif delta == 0:
    x1 = (-valorb +math.sqrt(delta))/(2*valora)
    print("\nX é igual a {0}".format(x1))
    print("O valor de delta é igual a {0}, portanto só temos um valor para x.\n".format(delta))
  else:
    x1 = (-valorb +math.sqrt(delta))/(2*valora)
    x2 = (-valorb -math.sqrt(delta))/(2*valora)
    print("\nX1 é igual a {0}".format(x1))
    print("X2 é igual a {0}".format(x2))
    print("O valor de delta é igual a {0}\n".format(delta))

  sair = input("Se deseja sair digite S, se não, aperte enter\n")
  if sair == "S" or sair == "s":
    break
