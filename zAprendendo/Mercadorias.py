
def compras():
  inicio = input("Deseja adicionar a mercadoria (S/N)?")
  if inicio == "S" or inicio == "s":
    quantidade = 1
    valor_mercadoria = int(input("Digite o valor da mercadoria: "))
    while True:
      mercadorias = input("Deseja adicionar mais dessa mercadoria (S/N)? ")
      if mercadorias == "S" or mercadorias == "s":
        quantidade = quantidade + 1
      elif mercadorias == "N" or mercadorias == "n":
        total_gasto = float(valor_mercadoria * quantidade)
        print("\nA quantidade total de mercadorias é de {}, totalizando R$:{}".format(quantidade, total_gasto))
        break
compras()
