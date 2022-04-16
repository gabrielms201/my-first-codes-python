import random


def pergunta1():
    print("Essa é a pergunta 1")
def pergunta2():
    print("Essa é a pergunta 2")
def pergunta3():
    print("Essa é a pergunta 3")


perguntas = [pergunta1,pergunta2,pergunta3]

cu = random.choice(perguntas)
perguntas.remove(cu)
cu()

#resposta[questao-1] != "A" and resposta[questao-1] != "B" and resposta[questao-1] != "C" and resposta[questao-1] != "D" and resposta[questao-1] != "E" :




