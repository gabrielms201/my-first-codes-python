
"""
Elabore um programa que leia notas de três avaliações de um aluno. A primeira avaliação tem
peso 2, a segunda tem peso 3 e, a terceira, peso 5. Calcule a média do aluno. Se a média do
aluno for maior ou igual a 6, o aluno está aprovado; caso contrário, o aluno está reprovado.
Mostre o resultado da decisão
"""

nota1 = float(input("\nDigite a sua primeira nota:\n"))
nota2 = float(input("Digite a sua segunda nota:\n"))
nota3 = float(input("Digite a sua terceira nota:\n"))
mediaFinal = round((nota1*2 + nota2*3 + nota3*5)/10, 2)

if mediaFinal >= 6:
  print(f"\nSua média final foi {mediaFinal}\nParabéns, você foi aprovado!")
else:
  print(f"\nSua média final foi {mediaFinal}\nInfelizmente você reprovou de ano...")

