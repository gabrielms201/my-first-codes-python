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

#Input
p1 = input("Telefonou para a vítima? (S/N)\n").lower()
p2 = input("Esteve no local do crime? (S/N)\n").lower()
p3 = input("Mora perto da vítima? (S/N)\n").lower()
p4 = input("Devia para a vítima? (S/N)\n").lower()
p5 = input("Já trabalhou com a vítima? (S/N)\n").lower()
#Processamento
def pergunta(p):
    if p == "s": return 1
    elif p == "n": return 0
def condicoes():
    if total == 5: return "Assassino"
    elif total == 3 or total == 4: return "Cúmplice"
    elif total == 2: return "Suspeita"
    else: return "Inocente"
total = pergunta(p1)+pergunta(p2)+pergunta(p3)+pergunta(p4)+pergunta(p5)
#Output
print(condicoes())


