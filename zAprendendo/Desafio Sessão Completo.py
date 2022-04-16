DataSessao = 23.00    
HoraSessao = 21.00

def Recepcionista(DataAtual, HoraAtual,MinutosExcedido):  
  HorárioExcedido = HoraSessao + MinutosExcedido #Apenas Teste
  print("Recepcionista: Tickets Por Favor") #Diálogo
  print("Cliente: Tome") #Diálogo 

  if DataSessao == DataAtual and HoraAtual > HoraSessao: #Checar se está atrasado
    print("Recepcionista: O tempo limite foi excedido!, pois a sessão é às", HoraSessao,"e você chegou às", HoraAtual) 
  elif DataSessao == DataAtual and HoraAtual < HoraSessao: #Checar se está adiantado
    print("Recepcionista: O horário da sessão é apenas às", HoraSessao,", e você chegou às", HoraAtual, "logo você não pode entrar ainda")
  elif DataSessao != DataAtual: #Checar se a data é incorreta
    print("Recepcionista: Volte no dia correto!")
  else: #Tudo está certo
    print("Recepcionista: Pode Entrar!")

Recepcionista(23.00, 22.00, 00.30)
