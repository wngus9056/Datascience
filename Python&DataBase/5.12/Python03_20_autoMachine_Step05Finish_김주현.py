menu = ['orange', 'strawberry', 'peach', 'mango', 'grape']
money = [1000, 2500, 1500, 2000, 2000]

print("******홍익 대학교 과일 판매머신 V03 ******")
for num in range(0,5):
	print(num + 1,'...', menu[num], money[num],"원")
print("6 ... exit")
print("="*40)

ex = (1, 2, 3, 4, 5, 6)

while True:
	number = input("구매번호를 입력하세요(1~5): ")
	number = int(number)
	if number == 6:         # 6을 입력하면
		print()
		print("종료합니다.")   # '종료합니다.'를 출력하고
		print()
		print("-" * 40)
		print()
		break               # break하며 반복문을 빠져나온다.
	elif number not in ex:  # 1~6 외의 숫자를 입력하면
		print()
		print("입력하신 번호 확인 바랍니다.")   # '입력하신 번호 확인 바랍니다.'를 출력하고
		print()
		print('-' * 40)
		continue            # while 문으로 돌아간다.
	coin = input("코인을 투입해주세요.")
	coin = int(coin)
	print("투입된 금액은 %d 원 입니다." %coin)
	print()
	print("=" * 40)
	print()
	if number in range(0,6):            # 만약 number가 0~5에 포함된다면
		dlddu = coin - money[number-1]  # money[number-1]하는 이유는 원하는 과일이 grape이면 사용자는 5를 입력하지만 grape인덱스는 4이다. 그래서 -1을 해준다.
		dlddu2 = coin                   # 투입한 돈에서 고른 과일 값을 빼준다.
		print()                         # 돈이 부족할 경우를 대비해 dlddu2를 만듦
		print("입력하신 구매번호는 %d 입니다." %number)
		print()
		print("선택한 과일 : ", menu[number-1], "은(는)", money[number-1], "원 입니다.")
		print()
		print("받은 금액은 %d 원 입니다." %coin)
		print()
		print("="*18, "거스름돈", "="*18)
		print()
		print("거스름돈은 %d 원 입니다." %dlddu)
		print()
		print()
		if dlddu < 0:
			print("금액이 부족합니다.")
			print()
			print("%d 원 반환해드리겠습니다." %dlddu2)
			print()
			print("-" * 40)



'''
while True:
	number = input("구매번호를 입력하세요(1~5): ")
	for i in number:
		i = int(i)
		print(menu[i-1], "은(는)", money[i-1], "원 입니다.")
		print("---------------------------------------")
		print()
'''




'''
while True:
	number = input("구매번호를 입력하세요(1~5): ")
	for i in number:
		i = int(i)
		print(menu[i-1], "은(는)", money[i-1], "원 입니다.")
		print("---------------------------------------")
		print()
	else:
		break
'''




'''
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
