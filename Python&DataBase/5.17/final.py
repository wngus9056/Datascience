

menu = ['1. 회원가입', '2. 로그인', '3. 회원목록', '9. 메뉴종료']
menuChk = ['1','2','3','9']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']


user_check = []

print('='*20, " 메뉴선택 ", '='*20, end='\n\n')
for x in range(4):
	print(menu[x], "  ", end='')
print(end= '\n\n')
print('='*52)

while True:
	number = input("\t메뉴의 번호를 선택해주세요.	")
	if number == '':
		print()
		print('숫자 확인하세요.')
		continue
	if number != '':
		number = int(number)
	if number == 9:
		print('종료합니다.')
		break
	if number not in range(1,4):
		print()
		print('숫자 확인하세요.', end='\n\n')
		continue
	else:
		user_list = []
		for y in range(1):
			if number == 1:
				print(end='\n\n')
				print("\tSign Up", end='\n\n')
				for z in range(6):
					chu = input('\t' + itemList[z] + '\t:\t')
					user_list.append(chu)
#				print(user_list)
				user_check.append(user_list)
				users = int(len(user_check))
				print()
#				print('\t', user_check, end = '\n')
#				print('\t현재 회원 수는 %d명 입니다.' %users)

				for i in range(users):
					print('\t', user_check[i])
				print('\t현재 회원 수는 %d명 입니다.' %users, end='\n\n')




	

