import random

while True:
  operadores = ["+", "-", "*"]
  op = random.choice(operadores)
  num1 = random.randint(1,100)
  num2 = random.randint(1,100)
  print(num1, op, num2)

  entrada = int(input("Resposta:"))
  def calc(a, b):
    if op == "+":
      return(a + b)
    elif op == "-":
      return(a - b)
    elif op == "*":
      return(a*b)

  if entrada == calc(num1, num2):
    print("Boa")
  else:
    print("Se fudeu")
  