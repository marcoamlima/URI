A, B, C = map(float, (input().split()))

delta = (B**2) -4 * A * C

if delta < 0:
    print("Impossivel calcular")
elif A == 0:
    print("Impossivel calcular")
else:
    r1 = (-B + ((delta)**(1/2))) / (2 * A)
    r2 = (-B - ((delta)**(1/2))) / (2 * A)
    print("R1 = %.5f" % r1)
    print("R2 = %.5f" % r2)
    