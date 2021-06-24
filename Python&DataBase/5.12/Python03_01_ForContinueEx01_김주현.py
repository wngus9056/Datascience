marks = [90, 25, 67, 45, 80]

number = 0

for a in marks:
	number = number + 1
	if a < 60:              # 반복문을 돌며 a가 60보다 작을 경우 9번 라인 print하지않고 for문으로 돌아가 다음 반복문을 실행한다.
		continue
	print(number, "번 학생은 합격입니다. 축하합니다.")