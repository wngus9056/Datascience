

while True:
	
	num =int(input("숫자를 입력하세요 :  [Exit : 0]"))
	
	if num==0:
		break
	
	elif num<20:
		print("20 이상의 수를 입력하세요")
	
	else:
		print("1.소수X")
		for j in range(2,num+1):
			a=0
			for i in range(2,j):
				if j % i==0:
					a=1
			if a==0:
				print("%d.소수O"%j)
			else:
				print("%d.소수X"%j)



while True:
	print()
	number = int(input("20이상의 수를 입력하세요 [ Exit : 0 ] : "))
	if number == 0:
		print()
		print("종료합니다.")
		print()
		break
	if number >= 20:
		for x in range(2, number+1):
			b = 0
			for j in (2, x):
				if x % j == 0:
					b = 1
				if b == 0:
					OX = "O"
				else:
					OX = "X"
			print("%d. 소수 %s." %(x, OX))
	else:
		print()
		print("숫자 확인하세요.")
		print()
		print('-' * 40)






'''
while True:
	number=int(input('20이상의 수를 입력하세요 [ Exit : 0 ]:'))
	print()
	print('='*60)

	if number>=20:
		b=0
		for i in range(2,number+1):
			for j in (2, i+1)
			if number%i==0:
				b=1
				if b==0:
					OX = "O"
				else:
					OX = "X"
				print()
				print('%d. 소수 %c.' %(i,OX))

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

