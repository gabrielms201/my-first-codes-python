qnt = int(input("Digite a quantidade de alunos: "))
alunos = range(0,qnt)
aprovados = []
reprovados = []

def nota(a):
    nota = float(input("Digite a nota %g do aluno: " % a))
    while nota < 1 or nota > 10:
        print("Digite uma nota válida...")
        nota = float(input("Digite a nota %g do aluno: " % a))
    return nota
        
for i in alunos: 
    nome = input("Digite o nome do aluno: ")
    nota1 = nota(1)
    nota2 = nota(2)
    media = (nota1+nota2)/2
    if media >= 6:
        aprovados.append(nome)
    else:
        reprovados.append(nome)
qnt_aprovados = len(aprovados)
qnt_reprovados = len(reprovados)

print("========================================================")
print("Alunos aprovados: %s\nAlunos reprovados: %s\n\n\t> Quantidade de aprovados: [%d]\n\t> Quantidade de reprovados: [%d] " 
% (aprovados, reprovados, qnt_aprovados, qnt_reprovados))
print("========================================================")


