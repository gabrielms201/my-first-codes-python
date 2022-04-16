"""
Escreva um programa que pergunte qual o valor incial de uma
divida e o juro mensal.Pergunte tembem o valor mensal que sera pago.Imprima o numero de meses para que a divida 
seja paga, o total pago e o total de juros pago
""" 

divida = 3200
jurosMensal = 0.1
valorMensal = 1
meses = 1

if (divida * (jurosMensal/100) > valorMensal):
  print("Nunca será possível pagar a sua dívida, já que os juros são maiores que o pagamento mensal")
else:
  saldo = divida
  jurosPago = 0 
  while saldo > valorMensal:
    juros = saldo * jurosMensal/100
    saldo = saldo + juros - valorMensal
    jurosPago = juros + jurosPago
    print("Seu saldo no mês {:d} é {:.2f}".format(meses, saldo))
    meses += 1
  
  print ("O total de mêses será: {}, com um saldo de {:.2f} e total de juros pago igual a: {:.2f}".format(meses-1, saldo, jurosPago))
