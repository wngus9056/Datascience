while True:
	number=int(input('20이상의 수를 입력하세요 [ Exit : 0 ]:'))
	print()
	print('='*60)

	if number>=20:
		b=0
		c = 0
		for x in range(number):
			c = c+1
			for i in range(2,number):
				if number%i==0: # 입력한 값을 2부터 입력한 값까지 나누었을 때 나머지가 0이면 b = 1
					b=1
			if b==0:
				print()
				print('%d. 소수 O.' %c)
			else:
				print()
				print('%d. 소수 X.' %c)

	elif number == 0:
		print()
		print("종료합니다.")
		print()
		break
	else:
		print()
		print('숫자 확인하세요.')
		print()









'''
while True:
	number=int(input('20이상의 수를 입력하세요 [ Exit : 0 ]:'))
	print()
	print('='*60)

	if number>=20:
		b=0
		for i in range(2,number):
			if number%i==0:
				b=1
		if b==0:
			print()
			print('%d. 소수 O.' %number)
			print()
		else:
			print()
			print('%d. 소수 X.' %number)
			print()

	elif number == 0:
		print()
		print("종료합니다.")
		print()
		break
	else:
		print()
		print('숫자 확인하세요.')
		print()
'''

