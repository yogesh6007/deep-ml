
def calculate_brightness(img):
	# Write your code here
	if not img:
		return -1
	if not img[0]:
		return -1
	cols = len(img[0])
	total=0
	count=0
	for row in img:
		if len(row) != cols:
			return -1
		for pixel in row:
			if pixel < 0 or pixel > 255:
				return -1
			total+=pixel
			count += 1
	return round(total/count,2)
