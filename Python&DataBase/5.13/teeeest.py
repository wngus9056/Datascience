




'''
	a=int(input('숫자를 입력하세요:'))

	if a>=20:
		b=0
		for i in range(2,a):
			if a%i==0:
				b=1
		if b==0:
			print('소수입니다')
		else:
			print('소수가 아닙니다')

	else:
		print('숫자를 다시 확인하세요')
		'''



'''
a = int(input("숫자를 입력하세요:"))

if a >= 20:
	b = 0
	for i in range(2,a):
		if a % i == 0:
			b = 1
		if b == 0:
			print("소수")
		else:
			print("숫자 다시")
'''



number = int(input("숫자를 입력하세요:"))

if number >= 20:
	b = 0
	for i in range(2,number):
		if number % i == 0:
			b = 1
		if b == 0:
			print("소수")
		else:
			print("숫자 다시")


