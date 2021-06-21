
menu = ['orange', 'strawberry', 'peach', 'mango', 'grape']
money = [1000, 2500, 1500, 2000, 2000]

print("******홍익 대학교 과일 판매머신 V03 ******")
for num in range(0,5):
	print(num + 1,'...', menu[num], money[num],"원")
print("6 ... exit")
print("====================================")



while True:
	num = int(input("구매번호를 입력하세요(1~6): "))
	print("l")
	if num == 1:
		print(menu[num-1], "는", money[num-1], "원입니다.")
		print("--------------------------------------")
	elif num == 2:
		print(menu[num-1], "는", money[num-1], "원입니다.")
		print("--------------------------------------")
	elif num == 3:
		print(menu[num-1], "는", money[num-1], "원입니다.")
		print("--------------------------------------")
	elif num == 4:
		print(menu[num-1], "는", money[num-1], "원입니다.")
		print("--------------------------------------")
	elif num == 5:
		print(menu[num-1], "는", money[num-1], "원입니다.")
		print("--------------------------------------")
	elif num == 6:
		break


'''
menu = ['orange', 'strawberry', 'peach', 'mango', 'grape', 'exit']
money = ['1000원 입니다.', '2500원 입니다.', '1500원 입니다.', '2000원 입니다.', '2000원 입니다.', ' ']

print("******홍익 대학교 과일 판매머신 V02 ******")
num = 0
for i in menu:
	print(num + 1, menu[num], money[num])
	num = num + 1
print("====================================")



while True:
	num = int(input("구매번호를 입력하세요(1~5): "))
	if num == 1:
		print("orange는 1000원입니다.")
	elif num == 2:
		print("strawberry는 2500원입니다.")
	elif num == 3:
		print("peach는 1500원입니다.")
	elif num == 4:
		print("mango는 2000원입니다.")
	elif num == 5:
		print("grape는 2000원입니다.")
	elif num == 6:
		break
'''







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
