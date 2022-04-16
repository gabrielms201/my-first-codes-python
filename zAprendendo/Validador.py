"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

print("Condições: \nNome: maior que 3 caracteres\nIdade: entre 0 e 150\nSalário: maior que zero\nSexo: f ou m\nEstado Civil: s, c, v, d\n")


#Validar Nome:
nome = str.title(input("Digite o seu nome: "))
while len(nome) < 3:
    nome = input("Nome inválido! Digite novamente: ")
print("Nome válido")
#Validar Idade:
idade = int(input("Digite a sua idade: "))
while idade <= 0 and idade >= 150:
    idade = int(input("Idade inválida! Digite novamente: ")) 
print("Idade válida")
#Validar Salário: 
salario = int(input("Digite o seu salário:"))
while salario <= 0:
    salario = float(input("Salário inválido! Digite novamente: "))
print("Salário válido")
#Validar Sexo:
sexo = str.lower(input("Digite o seu sexo: "))
while sexo != "f" and sexo != "m":
    sexo = str.lower(input("Sexo inválido! Digite novamente: "))
print("Sexo válido")
#Validar Estado Civil:
estadoCivil = str.lower(input("Digite o seu Estado Civil: "))
while estadoCivil != "s" and estadoCivil != "c" and estadoCivil != "v" and estadoCivil != "d":
    estadoCivil = str.lower(input("Estado civil inválido! Digite novamente: "))
print("Estado Civil válido")
    
