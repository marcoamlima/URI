hi, mi, hf, mf = map(int, input().split())

th = 0
tm = 0

th = hf - hi
tm = mf - mi

if (hi == hf) and ((mi == mf) or (mi > mf)) :
    th = 24
elif (hf < hi):
    th = 24 - hi + hf
if mf < mi:
    tm = 60 - mi + mf
    th -= 1
print("O JOGO DUROU",th,"HORA(S) E",tm,"MINUTO(S)")
