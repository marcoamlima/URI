hi, hf = map(int, input().split())

th = 0

th = hf - hi

if hf == hi:
    th = 24
elif hf < hi:
    th = 24 - hi + hf

print("O JOGO DUROU",th,"HORA(S)")
