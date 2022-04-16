"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
1- "Telefonou para a vítima?"
2- "Esteve no local do crime?"
3- "Mora perto da vítima?"
4- "Devia para a vítima?"
5- "Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".
"""

p1 = [input("Telefonou para a vítima? (S/N)\n").lower()]
p2 = [input("Esteve no local do crime? (S/N)\n").lower()]
p3 = [input("Mora perto da vítima? (S/N)\n").lower()]
p4 = [input("Devia para a vítima? (S/N)\n").lower()]
p5 = [input("Já trabalhou com a vítima? (S/N)\n").lower()]
total = p1+p2+p3+p4+p5

for e in range(total.count("n")):
    total.remove("n")

tamanho = len(total)
if tamanho == 5: print("Assassino")
elif tamanho == 3 or tamanho == 4: print("Cúmplice")
elif tamanho == 2: print("Suspeita")
else: print("Inocente")







