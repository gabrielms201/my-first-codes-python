lista = []
soma = 0
while True:
  inputNum = input("Digite o número: ")
  if inputNum == "":
    for e in lista:
      soma += e
    print("A soma é {}".format(soma))
    lista.clear();lista.append(soma)
    soma = 0
  elif inputNum == "zerar":
    lista.clear()
  elif inputNum == "sair":
    break
  else: 
    lista.append(float(inputNum))
    print(lista)


