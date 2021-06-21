print("******홍익 대학교 과일 판매머신 V01 ******")
print("1. orange				: 1000 원")
print("2. strawberry			: 2500 원")
print("3. peach				: 1500 원")
print("4. mango				: 2000 원")
print("5. grape				: 2000 원")
print("6. 종료")
print("====================================")



while True:                                         # 계속 반복
	num = int(input("구매번호를 입력하세요(1~5): "))
	if num == 1:
		print("orange는 1000원입니다.")
	if num == 2:
		print("strawberry는 2500원입니다.")
	if num == 3:
		print("peach는 1500원입니다.")
	if num == 4:
		print("mango는 2000원입니다.")
	if num == 5:
		print("grape는 2000원입니다.")
	if num == 6:                                    # num이 6이면 break해서 반복문을 빠져나온다.
		break



'''
print("******홍익 대학교 과일 판매머신 V01 ******")
print("1. orange				: 1000 원")
print("2. strawberry			: 2500 원")
print("3. peach				: 1500 원")
print("4. mango				: 2000 원")
print("5. grape				: 2000 원")
print("6. 종료")
print("====================================")



num = int(input("구매번호를 입력하세요(1~5): "))

while num != 6:
	if num == 1:
		print("orange는 1000원입니다.")
		num = int(input("구매번호를 입력하세요(1~5): "))
	if num == 2:
		print("strawberry는 2500원입니다.")
		num = int(input("구매번호를 입력하세요(1~5): "))
	if num == 3:
		print("peach는 1500원입니다.")
		num = int(input("구매번호를 입력하세요(1~5): "))
	if num == 4:
		print("mango는 2000원입니다.")
		num = int(input("구매번호를 입력하세요(1~5): "))
	if num == 5:
		print("grape는 2000원입니다.")
		num = int(input("구매번호를 입력하세요(1~5): "))
	if num == 6:
		break
'''
