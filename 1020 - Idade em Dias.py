tempo = int(input())

anos = int(tempo/365)
meses = int((tempo - (anos * 365)) / 30)
dias = tempo - (anos * 365) - (meses * 30)

print(anos,"ano(s)")
print(meses,"mes(es)")
print(dias,"dia(s)")
