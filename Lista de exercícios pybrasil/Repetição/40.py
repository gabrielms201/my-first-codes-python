# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
# Código da cidade;
# Número de veículos de passeio (em 1999);
# Número de acidentes de trânsito com vítimas (em 1999). 
# Deseja-se saber:
# Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# Qual a média de veículos nas cinco cidades ;
# Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
qntCidades = 5
menor = 9999999999999999999999999999999999999999999
maior = 0


somaVeiculos = 0
somaAcidentes = 0
qntAcidente = 0


for i in range(1,qntCidades+1):
    print("\tCidade número %d: " % i)

    codigo = int(input("Digite o código da cidade: "))
    veiculos = int(input("Digite o número de veículos de passeio da cidade: "))
    acidentes = int(input("Digite o número de acidentes de trânsito com vítimas:"))
    if acidentes < menor:
        menor = acidentes
        codigoMaior = codigo
    if acidentes > maior:
        maior = acidentes
        codigoMenor = codigo
    if veiculos < 2000:
        qntAcidente +=1
        somaAcidentes += acidentes
    somaVeiculos += veiculos

if qntAcidente >= 1:
    mediaAcidentes = somaAcidentes/qntAcidente
else:
    mediaAcidentes = "Não houve média de acidentes de trânsito nessa condição pois não possuem cidades com menos de 2.000 veículos."
mediaVeiculos = somaVeiculos / qntCidades

print("Maior índice: %.2f - Código da cidade: %.2f\nMenor índice: %.2f - Código da cidade: %.2f " %  (maior, codigoMaior, menor, codigoMenor))
print("Média de veículos: %.2f " % mediaVeiculos)
print("A média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio: %g " % (mediaAcidentes))
