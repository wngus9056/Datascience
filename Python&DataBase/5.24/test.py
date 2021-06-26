

# 묵 찌 빠
#  1  2  3


import random


cwin = 0
uwin = 0
draw = 0
whowin = []
win_total = 0




def defnum1():
	global uwin
	global cwin
	if computer == 1:
		print('\tCom : 바위\t/\tUser : 바위\t\t Draw! 비겼습니다!')
	elif computer == 2:
		print('\tCom : 가위\t/\tUser : 바위\t\t You Win! 당신이 이겼습니다!')
		uwin = uwin +1
	elif computer == 3:
		print('\tCom : 보\t/\tUser : 바위\t\t You Lose! 당신이 졌습니다!')
		cwin = cwin +1

def defnum2():
	global uwin
	global cwin
	if computer == 1:
		print('\tCom : 바위\t/\tUser : 가위\t\t You Lose! 당신이 졌습니다!')
		cwin = cwin+1
	elif computer == 2:
		print('\tCom : 가위\t/\tUser : 가위\t\t Draw! 비겼습니다!')
	elif computer == 3:
		print('\tCom : 보\t/\tUser : 가위\t\t You Win! 당신이 이겼습니다!')
		uwin = uwin+1

def defnum3():
	global uwin
	global cwin
	if computer == 1:
		print('\tCom : 바위\t/\tUser : 보\t\t You Win! 당신이 이겼습니다!')
		uwin = uwin+1
	elif computer == 2:
		print('\tCom : 가위\t/\tUser : 보\t\t You Lose! 당신이 졌습니다!')
		cwin = cwin+1
	elif computer == 3:
		print('\tCom : 보\t/\tUser : 보\t\t Draw! 비겼습니다!')

def defnum4():
	win_total = cwin + uwin
	if cwin > uwin:
		whowin = '패배'
		print('총 %d회의 게임 중 컴퓨터가 %d회, 당신이 %d회 이겼습니다.'%(win_total, cwin, uwin))
		print('따라서 최종 스코어 %d : %d ( 컴퓨터 : 당신 )로 당신의 %s입니다.'%(cwin, uwin, whowin))
	elif cwin == uwin:
		print('총 %d회의 게임 중 컴퓨터가 %d회, 당신이 %d회 이겼습니다.'%(win_total, cwin, uwin))
		print('따라서 최종 스코어 %d : %d ( 컴퓨터 : 당신 )로 무승부입니다.'%(cwin, uwin))
	else:
		whowin = '승리'
		print('총 %d회의 게임 중 컴퓨터가 %d회, 당신이 %d회 이겼습니다.'%(win_total, cwin, uwin))
		print('따라서 최종 스코어 %d : %d ( 컴퓨터 : 당신 )로 당신의 %s입니다.'%(cwin, uwin, whowin))
	



while True:
	computer = random.randint(1,3)
	user_input = input('번호를 선택하세요 : ')
	if user_input == '':
		print('숫자를 입력해주세요.')
		continue
	else:
		user_input = int(user_input)
		if user_input == 9:
			print('종료합니다.')
			break
		elif user_input not in range(1,5):
			print('숫자를 확인해주세요.')
		elif user_input == 1:
			defnum1()
		elif user_input == 2:
			defnum2()
		elif user_input == 3:
			defnum3()
		elif user_input == 4:
			defnum4()

