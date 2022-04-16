"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd' 
"""
#Validação do nome: 
nome = input("Digite o seu nome: (maior que 3 caracteres): ")
while len(nome) <= 3:
    print("Nome inválido...")
    nome = input("Digite o seu nome: (maior que 3 caracteres) ")
print("Informação válida")

#Validação da idade: 
idade = int(input("Digite a sua idade: (Entre 0 e 150 anos): "))
while idade <= 0 or idade >= 150: 
    print("Idade inválida...")
    idade = int(input("Digite a sua idade: (Entre 0 e 150 anos): "))
print("Informação válida")

#Validação do salário:
salario = float(input("Digite o seu salário: (maior que 0): "))
while salario <= 0: 
    print("Salário inválido...")
    salario = float(input("Digite o seu salário: "))
print("Informação válida")

#Validação do sexo: 
sexo = str.lower(input("Digite o seu sexo: (f ou m): "))
while sexo != "f" and sexo != "m":
    print("Sexo inválido...")
    sexo = str.lower(input("Digite o seu sexo: "))
print("Informação válida")

#Validação do estado civil
estado_civil = str.lower(input("Digite o seu estado civil: (s,c,v,d): "))
while estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil and "d":
    print("Estado civil inválido...")
    estado_civil = str.lower(input("Digite o seu estado civil: (s,c,v,d): "))
print("Informação válida")

