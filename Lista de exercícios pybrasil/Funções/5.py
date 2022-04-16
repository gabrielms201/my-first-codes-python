# Faça um programa com uma função chamada somaImposto.
# A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. 
# A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto,custo):
    custo = custo + (taxa/100 * custo)
    return custo
num = float(input("Digite o custo inicial: "))
taxa = float(input("Digite o valor de imposto: "))
print("Valor final: %.2f " % somaImposto(taxa, num))



