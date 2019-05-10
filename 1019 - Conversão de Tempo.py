tempo = int(input())

horas = int(tempo /3600)
minutos = int((tempo - (horas * 3600)) /60)
segundos = tempo - (horas * 3600) - (minutos * 60)

print(horas,minutos,segundos,sep=':')
