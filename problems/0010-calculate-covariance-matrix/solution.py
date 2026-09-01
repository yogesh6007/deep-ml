def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	n=len(vectors)
	means=[sum(vector)/len(vector) for vector in vectors]
	covariance=[]
	for i in range(n):
		row=[]
		for j in range(n):
			cov=sum((vectors[i][k]-means[i])*
					 (vectors[j][k]-means[j])
					 for k in range(len(vectors[i]))
					 )/(len(vectors[i])-1)
			row.append(cov)
		covariance.append(row)
	return covariance