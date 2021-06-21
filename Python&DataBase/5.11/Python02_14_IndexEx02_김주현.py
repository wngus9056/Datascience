'''
문제. range() 함수를 적용해서 동일결과 출력하기
90, 25, 67, 45, 80
'''
marks = [90, 25, 67, 45, 80]

for idx in range(0,5):  # 0~4까지 숫자를 idx에 반복하며 저장
	print(marks[idx])   # 0~4까지 반복하며 marks[0], marks[1]...marks[4] 출력