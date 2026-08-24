import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	rows,cols=new_shape
	total_elements=len(a)*len(a[0])
	required_elements=rows*cols
	if total_elements != required_elements:
		return[]
	return np.array(a).reshape(new_shape).tolist()