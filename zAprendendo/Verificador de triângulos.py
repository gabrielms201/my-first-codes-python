#Objetivo: Faça o usuário determinar os três lados de um triângulo. 
#Se ele existir, diga ao usuário o tipo de triângulo. Caso ele não exista, informe o usuário e peça para tentar novamente.

#> Funções:
def lados(): #Função para retornar o input ao usuário
  global a;global b; global c
  a = float(input("Digite o valor do lado a: "))
  b = float(input("Digite o valor do lado b: "))
  c = float(input("Digite o valor do lado c: "))
def existencia(): #Função que retorna a condição de existência de um triângulo
  if abs(b-c) < a < (b+c) and abs(a-c) < b < (a+c) and abs(a-b) < c < (a+b):
    return True
  else:
    return False
def tipo(): #Função que indentifica o tipo do triângulo, caso ele exista
  if a == b == c:
    return("Os valores {}, {}, {} são capazes de formar um triângulo. Sendo ele equilátero".format(a,b,c))
  elif a==b or b==c or a==c:
    return("Os valores {}, {}, {} são capazes de formar um triângulo. Sendo ele isóceles".format(a,b,c))
  else: 
    return("Os valores {}, {}, {} são capazes de formar um triângulo. Sendo ele escaleno".format(a,b,c))
#> Programa
while True: #Programa principal, que chama a função de input e faz um loop caso o usuário não desejar sair do programa
  lados()
  if existencia() == True:
    print(tipo())
    sair = input("Deseja sair? (S/N) ")
    if sair == "s" or sair == "S":break
  else: 
    print("\nOs valores fornecidos não são capazes de formar um triângulo. \nDetermine valores que são condizentes com a condição de existência.\n")
