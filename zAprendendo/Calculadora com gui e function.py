#Funções de cálculo:
def calcSoma(a,b): #Cálculo da soma
  return(a+b)
def calcSub(a,b): #Cálculo da subtração
  return(a-b)
def calcMult(a,b): #Cálculo da multiplicação
  return(a*b)
def calcDiv(a,b): #Cálculo da divisão
  return(a/b)
#Funções de input, menu e processamento
def numeros(): #Input dos números
  global num1
  global num2
  num1 = int(input("Digite o primeiro número:\n"))
  num2 = int(input("Digite o segundo número:\n"))
def gui(): #Interface do menu
  print("\n**********************************************************************")
  print("Calculadora. Opções Disponíveis:")
  print("*1.Adição")
  print("*2.Subtração")
  print("*3.Multiplicação")
  print("*4.Divisão")
  print("*5.Sair do programa")
  print("**********************************************************************\n")
  calculos()
def calculos(): #Programa principal (cálculos) ; Processamento
  escolha = int(input("Digite a opção desejada: "))
  if escolha == 1:
    numeros()
    soma = calcSoma(num1, num2)
    print("\nO valor da soma entre esses valores é igual a: {}".format(soma))
    gui()
    
  elif escolha == 2:
    numeros()
    sub = calcSub(num1, num2)
    print("\nO valor da subtração entre esses valores é igual a: {}".format(sub))
    gui()

  elif escolha == 3:
    numeros()
    mult = calcMult(num1, num2)
    print("\nO valor da multiplicação entre esses valores é igual a: {}".format(mult))
    gui()

  elif escolha == 4:
    numeros()
    div = calcDiv(num1, num2)
    print("\nO valor da divisão entre esses valores é igual a: {}".format(div))
    gui()

  elif escolha == 5:
    return False
    
  else:
    print("Por favor, entre com uma opção válida")
    gui()
#Chamando o menu, que mais tarde vai chamar o programa
gui() 