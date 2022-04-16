# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

c1 = 0
c2 = 0
c3 = 0

n = int(input("Digite o número total de eleitores: "))

for i in range(n):
    voto = input("Digite em qual candidato votar: (c1,c2,c3) ")
    while voto != "c1" and voto != "c2" and voto != "c3":
        voto = input("Voto inválido.\nDigite em qual candidato votar: (c1,c2,c3) ")
    if voto == "c1":
        c1 +=1
    elif voto == "c2":
        c2 +=1
    elif voto == "c3":
        c3 +=1      
print("Total de votos para c1:%d\nTotal de votos para c2:%d\nTotal de votos para c3:%d" % (c1,c2,c3))       
