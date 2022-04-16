# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:
# Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
# 1                                          0
# 3                                          10
# 6                                          15
# 9                                          20
# 12                                         25
# Exemplo de saída do programa:
# Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
# R$ 1.000,00     0               1                       R$  1.000,00
# R$ 1.100,00     100             3                       R$    366,00
# R$ 1.150,00     150             6                       R$    191,67

divida = 1000
parcela = 1
print("\nValor da dívida\tValor do Juros\tQuantidade de Parcelas\tValor da parcela")
for i in range(5):
    if i == 0:
        juros = 0
        parcela = 1
    elif i == 1:
        juros = 10
        parcela = 3
    elif i == 2:
        juros += 5
        parcela = 6
    elif i == 3:
        juros += 5
        parcela = 9
    elif i == 4:
        juros += 5
        parcela = 12
    

    total = divida + divida*juros/100
    # print("\nValor da dívida = %.2f" % total)
    # print("Valor do Juros = %.2f " % (total - divida))
    # print("Quantidade de parcelas: %d" % parcela )
    # print("Valor da parcela: %.2f " % (total/parcela))

    print("R$: %.2f\tR$: %.2f\t%d\t\t\tR$:%.2f" % (total,total-divida,parcela,total/parcela))