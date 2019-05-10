x, y = map(int, input().split())
while x != 0 and y != 0:
	if x >= 1 and y >= 1:
		print("primeiro")
	elif x >= 1 and y <= -1:
		print("quarto")
	elif x <= -1 and y >= 1:
		print("segundo")
	elif x <= -1 and y <= -1:
		print("terceiro")
	x, y = map(int, input().split())
	