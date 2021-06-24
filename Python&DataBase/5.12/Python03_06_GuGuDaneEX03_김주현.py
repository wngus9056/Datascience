for x in range(2,4):        # outer : 2             outer : 3
	print("outer : ", x)
	for y in range(1,4):    # inner : 1, 2, 3       inner : 1, 2, 3
		print("inner : ", y, end='  ')
	print()
	print()