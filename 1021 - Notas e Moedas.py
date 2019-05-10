valor = float(input())

aux = valor
troco = int(valor)
moedas = int(round((aux - troco) * 100, 0))

cem = int(troco/100)
troco = troco - (cem*100)

cinquenta = int(troco/50)
troco = troco - (cinquenta*50)

vinte = int(troco/20)
troco = troco - (vinte*20)

dez = int(troco/10)
troco = troco - (dez*10)

cinco = int(troco/5)
troco = troco - (cinco*5)

dois = int(troco/2)
troco = troco - (dois*2)

um = int(troco/1)
troco = troco - (um*1)

cc = int(moedas/50)
moedas = moedas - (cc*50)

vcc = int(moedas/25)
moedas = moedas - (vcc*25)

dc = int(moedas/10)
moedas = moedas - (dc*10)

ccc = int(moedas/5)
moedas = moedas - (ccc*5)

uc = moedas

print("NOTAS:")
print(cem,"nota(s) de R$ 100.00")
print(cinquenta,"nota(s) de R$ 50.00")
print(vinte,"nota(s) de R$ 20.00")
print(dez,"nota(s) de R$ 10.00")
print(cinco,"nota(s) de R$ 5.00")
print(dois,"nota(s) de R$ 2.00")

print("MOEDAS:")
print(um,"moeda(s) de R$ 1.00")
print(cc,"moeda(s) de R$ 0.50")
print(vcc,"moeda(s) de R$ 0.25")
print(dc,"moeda(s) de R$ 0.10")
print(ccc,"moeda(s) de R$ 0.05")
print(uc,"moeda(s) de R$ 0.01")
