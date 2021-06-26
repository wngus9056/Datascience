

# 묵 찌 빠
#  1  2  3
import random


while True:
	computer = []
	user_input = input('번호를 선택하세요 : ')
	computer = random.randint(1,3)
	if user_input == 1:
		if computer == 1:
			print('\tCom : 바위\t/')
