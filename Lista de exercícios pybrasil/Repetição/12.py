num = int(input("Digite o número que deseja ver a tabuada: "))
if num >= 1 and num <= 10:
    print("\nTabuada do {}:".format(num))
    for i in range(10):
        i +=1
        print("{} x {} = {}".format(num,i,num*i))
else:
    print("Especifique um valor entre 1 e 10...")
