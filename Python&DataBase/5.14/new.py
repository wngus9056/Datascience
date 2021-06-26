

chk = []
chk_count = []

while True:
	number = int(input("^10 이상의 수를 입력해주세요 [ Exit : 0 ] : "))
	if number >= 10:
		print("==<< %d번 반복합니다. >>==" %number)
		for x in range(1, number+1):
			if x % 3 == 0:
				chk.append("Apple")
			if x % 4 == 0:
				chk.append("Melon")
			if x % 5 == 0:
				chk.append("Grape")
			if x % 8 == 0:
				chk.append("StrawBerry")
			chk_count = chk_count + chk
			if len(chk) == 0:
				print("%d. " %x)
			else:
				print("%d. " %x, str(chk))
			chk = []

		print("==<< Fruit Counter List >>==")
		print("Apple : %d회" %chk_count.count("Apple")
		print("Melon : %d회" %chk_count.count("Melon")
		print("Grape : %d회" %chk_count.count("Grape")
		print("StrawBerry : %d회" %chk_count.count("StrawBerry")

	elif number == 0:
		print("종료합니다.")
	else:
		print("^숫자 확인하세요.")
			
