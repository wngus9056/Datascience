

# 묵 찌 빠
#  2  1  3


import random


cwin = 0
uwin = 0
draw = 0
whowin = []
num_total = 0




def defnum1():
	global uwin
	global cwin
	global num_total
	if computer == 1:
		num_total += 1
		print('\tCom : 가위  /  User : 가위\t You Draw! 비겼습니다!',end='\n\n')
		print('\t=> 현재 스코어 %d : %d ( 컴퓨터 : 당신 ) 입니다.'%(cwin, uwin))
		print()
	elif computer == 2:
		num_total += 1
		print('\tCom : 바위  /  User : 가위\t You Lose! 당신이 졌습니다!',end='\n\n')
		cwin += 1
		print('\t=> 현재 스코어 %d : %d ( 컴퓨터 : 당신 ) 입니다.'%(cwin, uwin))
		print()
	elif computer == 3:
		num_total += 1
		print('\tCom : 보  /  User : 가위\t You Win! 당신이 이겼습니다!',end='\n\n')
		uwin += 1
		print('\t=> 현재 스코어 %d : %d ( 컴퓨터 : 당신 ) 입니다.'%(cwin, uwin))
		print()

def defnum2():
	global uwin
	global cwin
	global num_total
	if computer == 1:
		num_total += 1
		print('\tCom : 가위\t/\tUser : 바위\t\t You Win! 당신이 이겼습니다!',end='\n\n')
		uwin += 1
		print('\t=> 현재 스코어 %d : %d ( 컴퓨터 : 당신 ) 입니다.'%(cwin, uwin))
		print()
	elif computer == 2:
		num_total += 1
		print('\tCom : 바위\t/\tUser : 바위\t\t Draw! 비겼습니다!',end='\n\n')
		print('\t=> 현재 스코어 %d : %d ( 컴퓨터 : 당신 ) 입니다.'%(cwin, uwin))
		print()
	elif computer == 3:
		num_total += 1
		print('\tCom : 보\t/\tUser : 바위\t\t You Lose! 당신이 졌습니다!',end='\n\n')
		cwin += 1
		print('\t=> 현재 스코어 %d : %d ( 컴퓨터 : 당신 ) 입니다.'%(cwin, uwin))
		print()

def defnum3():
	global uwin
	global cwin
	global num_total
	if computer == 1:
		num_total += 1
		print('\tCom : 가위\t/\tUser : 보\t\t You Lose! 당신이 졌습니다!',end='\n\n')
		cwin += 1
		print('\t=> 현재 스코어 %d : %d ( 컴퓨터 : 당신 ) 입니다.'%(cwin, uwin))
		print()
	elif computer == 2:
		num_total += 1
		print('\tCom : 바위\t/\tUser : 보\t\t You Win! 당신이 이겼습니다!',end='\n\n')
		uwin += 1
		print('\t=> 현재 스코어 %d : %d ( 컴퓨터 : 당신 ) 입니다.'%(cwin, uwin))
		print()
	elif computer == 3:
		num_total += 1
		print('\tCom : 보\t/\tUser : 보\t\t Draw! 비겼습니다!',end='\n\n')
		print('\t=> 현재 스코어 %d : %d ( 컴퓨터 : 당신 ) 입니다.'%(cwin, uwin))
		print()

def defnum4():
	if cwin > uwin:
		whowin = '패배'
		print('\t총 %d회의 게임 중 컴퓨터가 %d회, 당신이 %d회 이겼습니다.'%(num_total, cwin, uwin))
		print('\t따라서 최종 스코어 %d : %d ( 컴퓨터 : 당신 )로 당신의 %s입니다.'%(cwin, uwin, whowin))
		print()
	elif cwin == uwin:
		print('\t총 %d회의 게임 중 컴퓨터가 %d회, 당신이 %d회 이겼습니다.'%(num_total, cwin, uwin))
		print('\t따라서 최종 스코어 %d : %d ( 컴퓨터 : 당신 )로 무승부입니다.'%(cwin, uwin))
		print()
	else:
		whowin = '승리'
		print('\t총 %d회의 게임 중 컴퓨터가 %d회, 당신이 %d회 이겼습니다.'%(num_total, cwin, uwin))
		print('\t따라서 최종 스코어 %d : %d ( 컴퓨터 : 당신 )로 당신의 %s입니다.'%(cwin, uwin, whowin))
		print()
	



while True:
	computer = random.randint(1,3)
	print('-'*70,end='\n\n')
	print('   1. 가위 \t2. 바위       3. 보 \t  4. 횟수입력\t 9. 종료',end='\n\n')
	user_input = input('\t번호를 선택하세요 : ')
	print()
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

