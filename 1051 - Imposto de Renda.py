sal = float(input())

if sal >= 0.00 and sal <= 2000.00:
    print("Isento")
elif sal >= 2001.00 and sal <= 3000.00:
    imp = ((sal - 2000.00)* 8) / 100
    print("R$ %.2f" % imp)
elif sal >= 3001.00 and sal <= 4500.00:
    imp = 1000 * 8 / 100 + (sal - 3000.01) * 18 / 100
    print("R$ %.2f" %imp)
elif sal > 4500.00:
    imp = 1000 * 8 / 100 + 1499.99 * 18 / 100 + (sal - 4500) * 28 / 100
    print("R$ %.2f" % imp)
    