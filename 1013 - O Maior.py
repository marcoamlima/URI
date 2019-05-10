a, b, c = map(int, input().split())
maiorab = (a+b+(abs(a-b))) / 2
if (c > maiorab):
    maior = c
else:
    maior = int(maiorab)

print(maior,"eh o maior")
