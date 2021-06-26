

menu = ['1. 회원가입', '2. 로그인', '3. 회원목록', '9. 메뉴종료']
menuChk = ['1','2','3','9']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']

user01 = []
user_check = []


print("="*15, " 메뉴선택 ", "="*15, end='\n\n')
print(menu[0],menu[1],menu[2],menu[3])
print()
print("="*15, " 메뉴선택 ", "="*15, end='\n\n')

while True:
	number = input("\t메뉴의 번호를 선택해주세요.  ")
	if number == "":
		print()
		print("숫자 확인하세요.")
		continue
	elif number != "":
		number = int(number)
	if number == 9:
		print("종료합니다.")
		break
	if number not in range(1,4):
		print()
		print("숫자 확인하세요.", end='\n\n')
		continue
	else:
		for x in range(1, number+1):
			if number == 1:
				print(end='\n\n')
				print("\tSign Up")
				ID = input("\tID\t:\t")
				user01.insert(0,ID)
				PWD = input("\tPWD\t:\t")
				user01.insert(0,PWD)
				NAME = input("\tNAME\t:\t")
				user01.insert(0,NAME)
				EMAIL = input("\tEMAIL\t:\t")
				user01.insert(0,EMAIL)
				PHONE = input("\tPHONE\t:\t")
				user01.insert(0,PHONE)
				ADDRESS = input("\tADDRESS\t:\t")
				user01.insert(0,ADDRESS)
				user02 = user01.reverse()
			user_check.append(user02)
			print(user01)
		continue








'''
			if number == x:
				print()
				print("\t\t", menu[number-1], " Algorithm Chk", end='\n\n')
'''



