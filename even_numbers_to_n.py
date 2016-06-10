def evenNumbersLst(num):
	evens = []
	for i in range(2, num + 1):
		if i % 2 == 0:
			evens.append(i)
	return evens

print(evenNumbersLst(20))
