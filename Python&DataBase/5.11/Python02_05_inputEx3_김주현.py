'''
문제. 실행시 2개의 값을 입력.
	   vId, vPwd
	   id가 'Orange'이고, pwd가 'HappyDay'이면 '반갑습니다. 회원님.' 아니면 '회원가입 확인 하세요.'
'''

'''
vId, vPwd = input('아이디와 패스워드를 띄어써서 입력해주세요 : ') .split()   # input으로 값을 받고 split으로 나눈 값을 각각 vId와 vPwd에 차례대로 담는다.


# vId = input("아이디를 입력해주세요: ")              # 결과는 위와 같다.
# vPwd = input("비밀번호를 입력해주세요: ")

if vId == 'Orange' and vPwd == 'HappyDay':      # vId가 'Orange'이고 vPwd가 'HappyDay'이면 '반갑습니다. 회원님.'을 출력한다.    
	print('반갑습니다. 회원님.')
elif vId == 'Orange' and vPwd != 'HappyDay':    # vId가 'Orange'이고 vPwd가 'HappyDay'이 아니라면 '비밀번호를 확인해주세요.'을 출력한다. 
	print("비밀번호를 확인해주세요.")
elif vId != 'Orange' and vPwd == 'HappyDay':    # vId가 'Orange'가 아니고 vPwd가 'HappyDay'이면 '아이디를 확인해주세요.'을 출력한다. 
	print("아이디를 확인해주세요.")
else:                                           # 아니라면 '회원 정보를 확인할 수 없습니다. 회원가입 해주세요.'를 출력한다.
	print('회원 정보를 확인할 수 없습니다. 회원가입 해주세요.')
'''


	#문제. 모든과목이 각각 40점을 넘기고 평균 60을 넘는다면 '합격' 아니라면 '불합격'

'''
Grade1, Grade2, Grade3 = input('1과목, 2과목, 3과목 점수를 띄어써서 입력해주세요 : ').split()  # 위와 동일

# Grade1 = input("1과목 점수를 입력해주세요: ")
# Grade2 = input("2과목 점수를 입력해주세요: ")
# Grade3 = input("3과목 점수를 입력해주세요: ")

ave = int(Grade1 + Grade2 + Grade3)

if int(Grade1) >= 40 and int(Grade2) >= 40 and int(Grade3) >= 40 and ave >= 60: # 1과목, 2과목, 3과목 점수가 40보다 높고 평균이 60보다 높으면 '합격을 축하드립니다.'를 출력한다.
	print("합격을 축하드립니다.")
else:                               # 아니라면 '불합격입니다.'를 출력한다.
	print("불합격입니다.")
'''


'''
Grade1 = int(input("1과목 점수를 입력해주세요: "))
Grade2 = int(input("2과목 점수를 입력해주세요: "))
Grade3 = int(input("3과목 점수를 입력해주세요: "))

ave = (int(Grade1 + Grade2 + Grade3) / 3)
if int(Grade1) >= 40 and int(Grade2) >= 40 and int(Grade3) >= 40 and ave >= 60:
	print("합격을 축하드립니다.")
elif int(Grade1) <40 and int(Grade2) >= 40 and int(Grade3) >= 40:
	print("1과목 점수가 부족합니다.")
elif int(Grade1) >= 40 and int(Grade2) < 40 and int(Grade3) >= 40:
	print("2과목 점수가 부족합니다.")
elif int(Grade1) >=40 and int(Grade2) >= 40 and int(Grade3) < 40:
	print("3과목 점수가 부족합니다.")
elif int(Grade1) >= 40 and int(Grade2) >= 40 and int(Grade3) >= 40 and ave < 60:
	print("평균이 부족합니다.")
else:
	print("불합격입니다.")
'''
