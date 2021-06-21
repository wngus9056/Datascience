a = 0
while a < 5:        # a가 5미만이면 반복한다.
	a = a + 1       # a가 0부터 1씩 증가하며 반복한다.
	if a ==3:       # 만약 a가 3이라면 더 이상 명령어를 진행하지 않고 while문으로 다시 돌아간다.
		continue
	print(a)