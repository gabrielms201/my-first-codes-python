import random
import math
import os
os.system("color 2")

def conta():
  while True:
    num = random.randrange(90,1000)
    calc = math.factorial(num)
    resul = str(calc).strip()
    print(resul)

conta()