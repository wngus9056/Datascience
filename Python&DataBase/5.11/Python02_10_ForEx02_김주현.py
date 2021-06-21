marks = [30, 60, 85, 92, 56]


number = 0
for mark in marks:                              # marks 리스트 안의 인덱스 0부터 끝까지 반복하며 mark 변수에 저장
	number = number +1                          # number가 0부터 1씩 증가하며 반복
	if mark >= 70:
		print("%d번 학생은 합격입니다." %number)     # %d 는 포맷형식으로 d는 숫자 포맷형식이다. 반복문이 처음 돌 때 number는 1이므로 1번 학새은...출력된다.
	else:
		print("%d번 학생은 불합격입니다." %number)


'''
number = 0
for mark in marks:
	number = number + 1
	if mark >= 70:
		print(number, "번 학생은 합격입니다.")
	else:
		print(number, "번 학생은 불합격합니다.")
'''