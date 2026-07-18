def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	result=[]
	if (len(a[0]) == len(b)):
		for row in a:
			product = 0
			for i in range(0, len(b)):
				product = product + (row[i]*b[i])
			result.append(product)
		return result
	else :
		return -1