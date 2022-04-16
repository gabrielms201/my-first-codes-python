import math

"""

Elabore	 um	 programa	 que	 calcular	 sua	 idade	 aproximada	 em	
segundos.	Para	tanto,	considere que o	programa	deve	trabalhar	com	
a	 data	 de	 1º.	 de	 janeiro	 de	 1990	 até	 a	 data	 presente.	 Para	 tanto,	
considere:

**	mês	(1-12)
**	dia	(1-31)
**	ano	(4	dígitos)

"""
anoDado = 1990
diaDado = 1
mesDado = 1

anoAtual = 2021
diaAtual = 28
mesAtual = 2

qntMeses = 12
qntDias = 31
mesesEmDias = qntMeses * qntDias



anosEmSegundos = (anoAtual-anoDado) * 31536000 # Anos que faltam multiplicado por quanto vale 1 ano em segundos
mesEmSegundos =  (mesAtual/qntMeses - mesDado/qntMeses) * 31536000 # Meses transformados em anos e dps multiplicados por qnts segundos vale 1 ano
diaEmSegundos = ((diaAtual/mesesEmDias) - (diaDado/mesesEmDias)) *31536000 #Dias transformados em anos e dps multiplicados por qnts segundos vale 1 ano

soma = anosEmSegundos + mesEmSegundos + diaEmSegundos

print(f"Você tem aproximadamente {soma} segundos de vida")





