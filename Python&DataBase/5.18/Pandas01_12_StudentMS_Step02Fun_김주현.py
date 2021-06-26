

menu = [' 1. 탈퇴학생 ', ' 2. 추가등록 ', ' 3. 학생목록 ', ' 4. 합격생목록 ',' 9. 메뉴종료 ']
menuChk = ['1','2','3', '4', '9']
itemList = ['ID','필기점수','실기점수','인성점수']
MenuList = ["ID", "필기", "실기" ,"인성","합계","평균","합격유무"]
idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],
      [89, 67, 46],[45, 86, 46],[68, 47, 98]]

Al = ['Algorithm Chk']

user_dic = {}



# 함수

def defdic():		#딕셔너리 넣는 함수
	for dic in range(len(idList)):
		user_dic[idList[dic]] = scoreList[dic]

def defmenu():	#메뉴 출력 함수
	print('-'* 100)
	print('학생관리시스템v02')
	print('-'* 100)

	for x in range(menu_len):
		print(menuChk[x]+ '. ', menu[x][4:],'    ', end='')
	print()
	print('-'* 100)

def defnum1():	#1번 입력시 출력할 함수
	print(menu[0], Al[0])

def defnum2():	#2번 입력시 출력할 함수
	print(menu[1], Al[0])

def defnum3():	#3번 입력시 출력할 함수
	for x in range(len(MenuList)):
		print(MenuList[x], end='\t')
	print()
	print('-'*60)
	for y in user_dic.keys():
		print(y, f'\t{user_dic[y][0]}\t{user_dic[y][1]}\t{user_dic[y][2]}\t{sum(user_dic[y])}\t{sum(user_dic[y])/3:<.2f}')

def defnum4():	#4번 입력시 출력할 함수
	print(menu[3], Al[0])

def defbone():	#while문
	while True:
		number = input('번호 입력: ')
		if number == '':
			print('번호를 입력하세요.')
			continue
		else:
			number = int(number)
			if number == 9:
				print('종료합니다.')
				break
			elif number not in range(1, 5):
				print('번호 확인하세요.')
				continue
			elif number == 1:
				defnum1()
			elif number == 2:
				defnum2()
			elif number == 3:
				defnum3()
			if number == 4:
				defnum4()




'''
dic = {}
deleteIDList = []
idx = 0
'''

defdic()


menu_len = len(menu)
il = range(len(idList))

defmenu()


defbone()
