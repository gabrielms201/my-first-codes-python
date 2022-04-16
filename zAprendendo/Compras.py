compras = []

while True:
    produto = str.lower(input("Digite o seu produto: "))
    if produto == "fim":
        print("×--------------------------------------------------------------------×")
        break
    quantidade = int(input("Digite a quantidade: "))
    preco = int(input("Digite o preco: "))
    compras.append([produto, quantidade, preco])

soma = 0 
print("Tabela de Preços:")
for e in compras:
    valor = e[1] * e[2]
    soma += valor
    print(" > Produto: [%s] > Quantidade: [%.2f] > Preco: [R$:%.2f]\n----» Valor total produto: R$:%.2f" % (e[0].title(),e[1],e[2],valor))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\n\n~~> Valor total da compra: R$:%.2f" % soma)
print("×--------------------------------------------------------------------×")