
'''
#1. 
grade = [1, 2, 3]
1.loop 적용
2. 합계
3. 평균 : len()
'''
grade = [80, 75, 55]
gsum = 0
for x in grade:
	gsum += x

ave = (gsum/len(grade))

print('# 문제 1.')
print('합계 : ', gsum)
print('평균 : ', ave)
print()
print('-'*15)

'''
#2.
int(input()) 숫자 입력
짝수 입니다.
홀수 입니다.
'''
print('# 문제 2.')
number = int(input('숫자를 입력하세요 : '))
if number % 2 == 0:
	print('짝수입니다.')
elif number % 2 ==1:
	print('홀수입니다.')
print()
print('-'*15)



'''
#3.
슬라이스
'''
print('# 문제 3.')
pin = '881120-1068234'
yyyymmdd = pin[:5]
num = pin[7:]
print('yyyymmdd : ',yyyymmdd, '\n'+'num : ', num)
print()
print('-'*15)

'''
#4.
1, 3 남자
2, 4 여자
'''
print('# 문제 4.')
pin01 = '881120-1068234'
gender = pin01[7]

if gender == '1' or gender == '3':
	print('남자입니다.')
elif gender == '2' or gender == '4':
	print('여자입니다.')
print()
print('-'*15)



'''
#5.
replace
'''
print('# 문제 5.')
a_5 = 'a:b:c:d'
a_5 = a_5.replace(':','#')
print(a_5)
print()
print('-'*15)

'''
#6.
sort
reverse
'''
print('# 문제 6.')
a_6 = [1, 3, 5, 4, 2]
a_6.sort()
a_6.reverse()
print(a_6)
print()
print('-'*15)

'''
#7.
join
'''
print('# 문제 7.')
a_7 = ['Life', 'is', 'too', 'short']
result_7 = " ".join(a_7)
print(result_7)
print()
print('-'*15)


'''
#8.
a + (4,)
'''
print('# 문제 8.')
a_8 = (1, 2, 3)
a_8 = a_8 + (4,)
print(a_8)
print()
print('-'*15)

'''
#9.
오류 이유
'''
print('# 문제 9.')
a_9 = dict()
print(a_9)
a_9['name'] = 'python'
a_9[('a',)] = 'python'
#a_9[[1]] = 'python' #리스트는 딕셔너리로 만들 수 없다.
a_9[250] = 'python'
print(a_9)


