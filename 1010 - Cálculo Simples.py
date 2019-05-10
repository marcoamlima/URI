codigo1, numero1, valor1 = map(float, input().split())
codigo2, numero2, valor2 = map(float, input().split())

preco1 = int(numero1) * valor1
preco2 = int(numero2) * valor2
total = preco1 + preco2

print("VALOR A PAGAR: R$ %.2f" %total)
