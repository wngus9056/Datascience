

while True:
	number = int(input("^10이상의 수를 입력 하세요. [ Exit : 0 ] : "))
	if number == 0:
		print("종료합니다.")
		break
	elif number < 10:
		print()
		print("^10이상의 숫자 확인 하세요.")
		print()
	elif number >= 10:
		print("==<< %d번 반복합니다. >>==" %number)
		ck = []
		ck_ct = []
		for x in range(1,number+1):
			if x % 3 == 0:
				ck.append("Apple")
			if x % 4 == 0:
				ck.append("Melon")
			if x % 5 == 0:
				ck.append("Grape")
			if x % 8 == 0:
				ck.append("StrawBerry")
			if len(ck) == 0:
				print("%d. " % x)
			else:
				print("%d. " %x, str(ck))
			ck_ct += ck
			ck = []
		print()
		print("==<< Fruit Count List >>====")
		print("Apple:			%d회" %ck_ct.count("Apple"))
		print("Melon:			%d회" %ck_ct.count("Melon"))
		print("Grape:			%d회" %ck_ct.count("Grape"))
		print("StrawBerry:		%d회" %ck_ct.count("StrawBerry"))
		print()
