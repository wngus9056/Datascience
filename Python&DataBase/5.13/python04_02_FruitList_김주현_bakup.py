# fruit = ['apple', 'melon', 'grape', 'strawberry']
# fcount = ['5 회', '3 회', '3 회', '1 회']



print()
print("==<< Fruit Count List >>====")
print("apple:			5회")
print("melon:			3회")
print("grape:			3회")
print("strawberry:		1회")
print()
print('-'*28)
print()

while True:
	'''
	print()
	print("==<< Fruit Count List >>====")
	print("apple:			5회")
	print("melon:			3회")
	print("grape:			3회")
	print("strawberry:		1회")
	print()
	'''

	number = int(input("10이상의 수를 입력 하세요. [ Exit : 0 ] : "))
	if number == 0:
		print("종료합니다.")
		break
	if number < 10:
		print()
		print("10이상의 숫자 확인 하세요.")
		print()
	elif number >= 10:
		print()
		print("==<< Fruit Count List >>====")
		print("apple:			5회")
		print("melon:			3회")
		print("grape:			3회")
		print("strawberry:		1회")
		print()
		print("==<< %d번 반복합니다. >>==" %number)
		for x in range(1,number+1):
			ck = []
			if x % 3 == 0:
				ck.append('Apple')
			if x % 4 == 0:
				ck.append("Melon")
			if x % 5 == 0:
				ck.append("Grape")
			if x % 8 == 0:
				ck.append("StrawBerry")
			for y in range(1, x+1):
				
				'''
				if x % 3 == 0:
					ck.append("Apple")
				if x % 4 == 0:
					ck.append("Melon")
				if x % 5 == 0:
					ck.append("Grape")
				if x % 8 == 0:
					ck.append("StrawBerry")
'''
				'''
				if x % 3 == 0:
					ck = [Apple]
				if x % 4 == 0:
					ck = [Melon]
				if x % 5 == 0:
					ck = [Grape]
				if x % 8 == 0:
					ck = [StrawBerry]
				if x % 4 == 0 and x % 8 == 0:
					ck = [Melon, StrawBerry]
			print("==<< 15번 반복합니다. >>==")
			'''
			print("%d. %s." %(x,ck))
