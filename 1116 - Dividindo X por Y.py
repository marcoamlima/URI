quant = int(input())

for x in range(quant):
    X, Y = map(float, input().split())
    if Y == 0:
        print("divisao impossivel")
    else:
        div = X / Y
        print("%.1f"%div)
        