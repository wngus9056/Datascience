

menu = ['1. 회원가입', '2. 로그인', '3. 회원목록', '9. 메뉴종료']
menuChk = ['1','2','3','9']

print("="*15, " 메뉴선택 ", "="*15, end='\n\n')
print(menu[0],menu[1],menu[2],menu[3])
print()
print("="*15, " 메뉴선택 ", "="*15, end='\n\n')

while True:
	number = int(input("\t메뉴의 번호를 선택해주세요.  "))
	if number == 9:
		print("종료합니다.")
		break
	if number not in range(1,4):
		print()
		print("숫자 확인하세요.", end='\n\n')
		continue
	for x in range(1, number+1):
		if number == x:
			print()
			print("\t\t", menu[number-1], " Algorithm Chk", end='\n\n')




