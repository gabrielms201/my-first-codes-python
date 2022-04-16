import math
import datetime
"""

Elabore	 um	 programa	 que	 calcular	 sua	 idade	 aproximada	 em	
segundos.	Para	tanto,	considere que o	programa	deve	trabalhar	com	
a	 data	 de	 1º.	 de	 janeiro	 de	 1990	 até	 a	 data	 presente.	 Para	 tanto,	
considere:

**	mês	(1-12)  
**	dia	(1-31)
**	ano	(4	dígitos)

"""
#Input
anoDado = 2003
diaDado = 27
mesDado = 4


#Obter tempo atual
dataAtual = datetime.datetime.now() 
anoAtual = float(dataAtual.strftime("%Y"))
diaAtual = float(dataAtual.strftime("%d"))
mesAtual = float(dataAtual.strftime("%m"))
segundosAtual = float(dataAtual.strftime("%S"))
horaAtual = float(dataAtual.strftime("%H"))
minutoAtual = float(dataAtual.strftime("%M"))

#Cálculo para ano bissexto
difAnos = anoAtual-anoDado
diasExtras = difAnos / 4.00
anoBissexto = (diasExtras / 365.00)*31536000.00

#Tempo convertido em segundos
anosEmSegundos = (anoAtual-anoDado) * 31536000.00 # Anos que faltam multiplicado por quanto vale 1 ano em segundos
mesEmSegundos =  (mesAtual/12.00 - mesDado/12.00) * 31536000.00 # Meses transformados em anos e dps multiplicados por qnts segundos vale 1 ano
diasEmSegundos = ((diaAtual/365.00 - diaDado/365.00)) *31536000.00 #Dias transformados em anos e dps multiplicados por qnts segundos vale 1 ano
horasEmSegundos = horaAtual*3600.00 #Horas atuais transformadas em segundos
minutosEmSegundos = minutoAtual*60.00 #Minutos atuais dados em segundos

#Output
soma = anosEmSegundos + mesEmSegundos + diasEmSegundos + horasEmSegundos + segundosAtual + anoBissexto + minutosEmSegundos
print(f"Você tem aproximadamente {soma} segundos de vida".replace(".",","))



