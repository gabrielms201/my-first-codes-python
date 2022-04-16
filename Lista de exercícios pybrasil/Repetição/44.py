# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
# 1 , 2, 3, 4  - Votos para os respectivos candidatos 
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.



print("Candidatos:\n1-João\n2-José\n3-Pedro\n4-Felipe\n5-Voto Nulo\n6-Voto em branco")
joao = 0
jose = 0
pedro = 0
felipe = 0 
nulo = 0
branco = 0

while True:
    voto = int(input("Digite o seu voto: (0 para sair)"))
    if voto == 0: break
    if voto == 1:
        joao += 1
    elif voto == 2:
        jose += 1
    elif voto == 3:
        pedro += 1
    elif voto == 4:
        felipe += 1
    elif voto == 5:
        nulo += 1
    elif voto == 6:
        branco += 1
    else:
        voto = int(input("\nCódigo de voto incorreto! Digite o seu voto: (0 para sair)"))

total = joao + jose + pedro + felipe + nulo + branco
if nulo > 0:
    porcentagemNulos = 100*nulo/total
else:
    porcentagemNulos = 0
if branco > 0:
    porcentagemBranco = 100*branco/total
else: 
    porcentagemBranco = 0

print("João: %d\nJosé: %d\nPedro:%d\nFelipe: %d\nNulos: %d\nBranco: %d" % (joao,jose,pedro,felipe,nulo,branco))
print("Porcentagem de votos nulos: %.2f%%\nPorcentagem de votos em branco: %.2f%%" % (porcentagemNulos, porcentagemBranco))


