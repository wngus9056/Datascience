

while True:

	number = int(input("10이상의 수를 입력 하세요. [ Exit : 0 ] : "))
	if number == 0:
		print("종료합니다.")
		break
	elif number < 10:
		print()
		print("10이상의 숫자 확인 하세요.")
		print()
	elif number >= 10:

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
			yee = len(ck)
		print()
		print("==<< Fruit Count List >>====")
		print("apple:			%d회" %yee)
		print("melon:			%d회" %yee)
		print("grape:			%d회" %yee)
		print("strawberry:		%d회" %yee)
		print()
				
		print("%d. %s." %(x,ck))
