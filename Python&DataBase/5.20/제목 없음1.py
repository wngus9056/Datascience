

a = []
while True:
    a.append(input('4인 이상의 이름을 입력하세요 (스페이스바로 구분) : ').split( ))
    if len(a) <4 :
        print('^ 명수를 확인하세요 ( 4인 이상 )')
    else:
        print(a, '입력되었습니다.')