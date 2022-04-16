
def Calculator(num1, num2, operator):
  
  if operator == "+": #Soma
    print(num1 + num2)
  elif operator == "-": #Subtração
    print(num1 - num2)
  elif operator == "*": #Multiplicação
    print(num1 * num2)
  elif operator == "/": #Divisão
    print(num1 / num2)
  else:
    print("Operador não especificado corretamente") #Caso o programa não reconhecer o sinal de operação
Valor1 = int(input("Primeiro Valor:")) # Informar o primeiro valor
Valor2 = int(input("Segundo Valor:")) # Informar o segundo valor 
Sinal = input("Digite qual será o sinal da operação: ") # Informar o sinal da operação desejada

Calculator(Valor1, Valor2, Sinal)