''' 문제. 실행시 점수를 입력받아 80점 이상이면 '합격입니다.'
          그렇지 않으면 '다음 기회에...'
'''


Grade = int(input())    # Grade변수에 int로 변환시킨 input값을 저장시킨다...숫자와 비교하기 위해서

if Grade >= 80:         # 위에서 int로 변환시켜주지 않았다면 if int(Grade) >= 80:
	print('합격입니다.')
else:
	print('다음 기회에...')