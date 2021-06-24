


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


