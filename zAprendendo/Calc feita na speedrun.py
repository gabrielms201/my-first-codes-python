def calcSoma(a,b):
  return (a+b)
def calcSub(a,b):
  return (a-b)
def calcMult(a,b):
  return (a*b)
def calcDiv(a,b):
  return(a/b)

def inputNum():
  global num1;global num2
  num1 = float(input("Digite o primeiro número: "))
  num2 = float(input("Digite o segundo número: "))

def escolha():
  escolha = input("Digite a opção desejada:")
  if escolha == "1":
    inputNum()
    print("\nA soma é: {}".format(calcSoma(num1,num2)))
    menu()
  elif escolha  == "2":
    inputNum()
    print("\nA subtração é: {}".format(calcSub(num1,num2)))
    menu()
  elif escolha == "3":
    inputNum()
    print("\nA multiplicação é: {}".format(calcMult(num1,num2)))
    menu()
  elif escolha == "4":
    inputNum()
    print("\nA divisão é: {}".format(calcDiv(num1,num2)))
  elif escolha == "5":
    print("Flw amigão")
    return False

def menu():
  print("\nBem vindo à calculadora. Por favor digite qual será a operação desejada:")
  print("1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Sair")
  escolha()



menu()