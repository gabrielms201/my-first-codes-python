"""
1) Um cinema possui capacidade de 100 lugares e está sempre com ocupação total. Certo dia,
cada espectador respondeu a um questionário, no qual constava:
- sua idade (superior ou igual a 14 anos)
- sua opinião em relação ao filme, segundo as seguintes notas:
Nota Significado
A       Ótimo
B        Bom
C      Regular
D       Ruim
E      Péssimo

Escreva um programa que, lendo esses dados, calcule e apresente:
a) a quantidade de respostas Ótimo;
b) a média de idade das pessoas que responderam Ruim;
c) a porcentagem de respostas Péssimo;
d) a maior idade entre as pessoas que responderam Bom;
e) a diferença entre a menor idade que respondeu Regular e a menor idade que respondeu Ruim.
"""

capacidade = int(input("Digite a capacidade do cinema: "))
contagem = capacidade
id_pessoa = 1

nota_otimo = 0
nota_bom = 0
nota_regular = 0
nota_ruim = 0
nota_pessimo = 0

#Parte B
soma_ruim = 0 
#Parte D
maior_bom = 0
#Parte E
menor_regular = 999999
menor_ruim = 999999


while contagem > 0:
    print("Sujeito número: %d" % id_pessoa) 
    idade = int(input("Digite a sua idade: (superior ou igual a 14 anos): "))

    if idade >=14:
        nota = str.lower(input("Digite a nota de sua opinião em relação ao filme, segundo as seguintes notas:\nNota\tSignificado:\nA\tÓtimo\nB\tBom\nC\tRegular\nD\tRuim\nE\tPéssimo:\n"))
        if nota == "a" or nota == "b" or nota == "c" or nota == "d" or nota == "e":
            if nota == "a":
                nota_otimo += 1
            elif nota == "b":
                nota_bom += 1
                if idade > maior_bom:
                    maior_bom = idade
            elif nota == "c":
                nota_regular += 1
                if idade < menor_regular:
                    menor_regular = idade
            elif nota == "d":
                nota_ruim += 1
                soma_ruim += idade
                if idade < menor_ruim:
                    menor_ruim = idade
            elif nota == "e":
                nota_pessimo += 1
            contagem -= 1
            id_pessoa += 1
        else:
                print("Nota incorreta.")
    else:
        print("Idade Incorreta.")

#Parte B
if nota_ruim == 0:
    media_ruim = soma_ruim
else: 
    media_ruim = soma_ruim / nota_ruim

#Parte C
porcentagem_pessimo = (100*nota_pessimo)/capacidade
diferenca = menor_regular - menor_ruim

print('a-) Quantidade de pessoas que responderam "ótimo": %d' % nota_otimo)    
print('b-) Média de idade das pessoas que responderam "ruim": %.2f' % media_ruim)
print('c-) Porcentagem de respostas "Péssimo": %.2f %% ' % porcentagem_pessimo)
print('d-) A maior idade entre as pessoas que responderam "Bom:" %d' % maior_bom)
print('e-) Diferença entre a menor idade daqueles que responderam "regular", e daqueles que responderam "ruim": %d' % diferenca)

