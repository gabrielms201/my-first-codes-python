# Uma funcao que inverte uma lista

lista = [1,2,3,4,5]

def inverter(lista):
    temp = []
    for i in range(len(lista)):
        temp.append(lista[len(lista)-1-i])
    return temp

print(inverter(lista))