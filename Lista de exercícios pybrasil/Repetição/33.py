# O Departamento Estadual de Meteorologia lhe contratou para desenvolver
# um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, 
# bem como a média das temperaturas.


temperatura = "0"
soma = 0
maior = 0
menor = 999999999
contador = 0
while temperatura != "fim":
    temperatura = input("Digite o valor da temperatura: (fim para sair): ")
    if temperatura != "fim":
        temp = float(temperatura)
        if temp < menor:
            menor = temp
        if temp > maior: 
            maior = temp
        soma += temp
        contador += 1
if contador > 0:
    media = soma/contador
else:
    media = "Não existe média pois nenhum valor foi informado"
print("Média de temperatura: %.2f" % media)