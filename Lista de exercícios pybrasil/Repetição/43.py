# O cardápio de uma lanchonete é o seguinte:
# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
# Considere que o cliente deve informar quando o pedido deve ser encerrado.
codigo = 1
soma = 0
preco = 0

while codigo != 0:
    codigo = int(input("Digite o código do produto: (0 para sair) "))
    if codigo == 0: break
    quantidade = int(input("Qual a quantidade desejada? "))
    if codigo == 100:
        preco = 1.2
    elif codigo == 101:
        preco = 1.3
    elif codigo == 102:
        preco = 1.5
    elif codigo == 103:
        preco = 1.2
    elif codigo == 104:
        preco = 1.3
    elif codigo == 105:
        preco = 1
    else: codigo = int(input("Código Inválido!\nDigite o código do produto: (0 para sair) "))
    soma += preco * quantidade
    print("%.2f x %d = %.2f" % (preco, quantidade, preco*quantidade))
    
print("Total: %.2f " % soma)