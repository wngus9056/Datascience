num = int(input("구매번호를 입력하세요(1~5): "))  # num 변수에 int로 변환한 input값을 저장

while num != 6:                             # num이 6이 아니면 반복
	if num == 1:                            # num이 1이면 'orange는 1000원입니다.'를 출력하고
		print("orange는 1000원입니다.")        # num 변수에 int로 변환한 input값을 저장
		num = int(input("구매번호를 입력하세요(1~5): "))
	elif num == 2:
		print("strawberry는 2500원입니다.")
		num = int(input("구매번호를 입력하세요(1~5): "))
	elif num == 3:
		print("peach는 1500원입니다.")
		num = int(input("구매번호를 입력하세요(1~5): "))
	elif num == 4:
		print("mango는 2000원입니다.")
		num = int(input("구매번호를 입력하세요(1~5): "))
	elif num == 5:
		print("grape는 2000원입니다.")
		num = int(input("구매번호를 입력하세요(1~5): "))
	elif num == 6:                          # num이 6이면 break해서 반복문을 빠져나온다.
		break