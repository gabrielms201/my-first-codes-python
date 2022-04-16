# Faça um programa que calcule o número médio de alunos por turma. 
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
# As turmas não podem ter mais de 40 alunos.

turmas = int(input("Digite a quantidade de turmas: "))
soma = 0

for i in range(turmas):
    alunos = int(input("Digite a quantidade de alunos da turma %d: " % (i+1)))
    while alunos > 40:
        alunos = int(input("Quantidade inválida. As turmas não podem ultrapassar 40 alunos!\nDigite a quantidade de alunos da turma %d: " % (i+1)))
    soma += alunos

media = soma/turmas
print("A média de alunos por turma é igual à: %.2f " % media)