

a = int(input("숫자 : ")
b = 0

for i in range(2,a):
	if a % i == 0:
		b = 1
if b == 0:
	print("소수")
else:
	print("아님")
