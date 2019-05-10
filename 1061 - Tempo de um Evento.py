valor = input().split()
di = int(valor[1])

valores = input().split(" : ")
hi,mi,si = list(map(int, valores))

valor = input().split()
df = int(valor[1])

valores = input().split(" : ")
hf,mf,sf = list(map(int, valores))

d = df - di
h = hf - hi
if h < 0 :
    h = 24 + 
    d = d - 1

m = mf - mi
if m < 0:
    m = 60 + m
    h = h - 1

s = sf - si
if s < 0:
    s = 60 + s
    m = m - 1
if d <= 0:
    d = 0

print("%d dia(s)" %d)
print("%d hora(s)" %h)
print("%d minuto(s)" %m)
print("%d segundo(s)" %s)
