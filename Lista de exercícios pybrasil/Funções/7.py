# Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. 
# O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valor
# Pagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. 
# Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação.
# Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. 
# O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. 
# Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
valor_total = qnt = 0
def valorPagamento(p,d):
    global valor_total, qnt
    if d <= 0:
        pagamento = p
    else:
        pagamento = p + ((3/100)*p + (0.1*d/100)*p)
    valor_total += pagamento
    qnt += 1
    return pagamento
while True:
    prestacao = int(input("Digite o valor da prestação: "))
    if prestacao == 0: break
    dias = int(input("Digite o número de dias em atraso: "))
    print("Valor total da prestação: R$: %.2f" % valorPagamento(prestacao,dias))
print("Relatório do dia:\nQuantidade de prestações pagas no dia: %d\nValor total de prestações:%.2f" % (qnt,valor_total))