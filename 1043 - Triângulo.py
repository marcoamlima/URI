A, B, C = map(float, input().split())

auxAB = A + B
auxBC = B + C
auxCA = C + A

if (auxAB > C) and (auxBC > A) and (auxCA > B):
    perimetro = A + B + C
    print("Perimetro =", perimetro)
else:
    area = ((A + B) * C ) / 2
    print("Area =", area)
    