n = int(input())

for i in range(n):
	x, y = map(int, input().split())
	soma = 0
	if x == y:
		print(0)
	else:
		aux = 0
		if x > y:
			aux = x
			x = y
			y = aux
		while x < y-1:
			x += 1
			if x % 2 != 0:
				soma += x
		print(soma)
		