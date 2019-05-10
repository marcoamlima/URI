sal  = float(input())

if sal >= 0 and sal <= 400.00:
    salf = sal + (sal*0.15)
    aum = salf - sal
    print("Novo salario: %.2f" % salf)
    print("Reajuste ganho: %.2f" % aum)
    print("Em percentual: 15 %")
elif sal >= 400.01 and sal <= 800.00:
    salf = sal + (sal * 0.12)
    aum = salf - sal
    print("Novo salario: %.2f" %salf)
    print("Reajuste ganho: %.2f" %aum)
    print("Em percentual: 12 %")
elif sal >= 800.01 and sal <= 1200.00:
    salf = sal + (sal * 0.10)
    aum = salf - sal
    print("Novo salario: %.2f" % salf)
    print("Reajuste ganho: %.2f" % aum)
    print("Em percentual: 10 %")
elif sal >= 1200.01 and sal <= 2000.00:
    salf = sal + (sal * 0.07)
    aum = salf - sal
    print("Novo salario: %.2f" % salf)
    print("Reajuste ganho: %.2f" % aum)
    print("Em percentual: 7 %")
elif sal > 1200.00:
    salf = sal + (sal * 0.04)
    aum = salf - sal
    print("Novo salario: %.2f" % salf)
    print("Reajuste ganho: %.2f" % aum)
    print("Em percentual: 4 %")
    