

menu = [' 1. 탈퇴학생 ', ' 2. 추가등록 ', ' 3. 학생목록 ', ' 4. 합격생목록 ',' 9. 메뉴종료 ']
menuChk = ['1','2','3', '4', '9']
itemList = ['ID','필기점수','실기점수','인성점수']
MenuList = ["ID", "필기", "실기" ,"인성","합계","평균","합격유무"]
Al = ['Algorithm Chk']


'''
idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],
      [89, 67, 46],[45, 86, 46],[68, 47, 98]];

dic = {}
deleteIDList = []
idx = 0
'''

menu_len = len(menu)


print('-'* 100)
print('학생관리시스템v01')
print('-'* 100)

for x in range(menu_len):
	print(menuChk[x]+ '. ', menu[x][4:],'    ', end='')
print()
print('-'* 100)


'''
print('-'* 100)
print('학생관리시스템v01')
print('-'* 100)

for x in range(5):
	print(menu[x],'    ', end='')
print()
print('-'* 100)
'''

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
		else:
			for y in range(4):
				if number == y+1:
					print(menu[y], Al[0])



'''
while True:
	number = input('번호 입력: ')
	if number == '':
		print('번호를 입력하세요.')
		continue
	elif number != '':
		number = int(number)
	elif number == 9:
		print('종료합니다.')
		break
	elif number not in range(1, 5):
		print('번호 확인하세요.')
		continue
	else:
		for y in range(4):
			if number == y+1:
				print(menu[y], Al[0])
'''