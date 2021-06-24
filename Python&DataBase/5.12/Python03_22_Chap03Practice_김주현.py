
## 문제 1. ##

'''
a = "Life is too short, you need python"

if "wife" in a : print("wife")                              # 만약 a안에 'wife'가 있으면 'wife' 출력
elif "python" in a and "you" not in a: print("python")      # a 안에 'python'이 있고 a 안에 'you'가 없으면 'python' 출력
elif "shirt" not in a: print("shirt")                       # a 안에 'shirt'가 없으면 'shirt' 출력
elif "need" in a: print("need")                             # a 안에 'need'가 있으면 'need' 출력
else: print("none")                                         # 아니면 'none' 출력
'''



## 문제 2. ##

'''
result = 0

a = 1
while a <1001:                  # a가 1001 이상이 될 때까지 반복
	if a %3 ==0:                # 만약 a가 3으로 나누어떨어지면 result += a
		result = result + a
	a = a+1
print(result)
'''




## 문제 3. ##

'''
a = 0

while a <5:             # a가 5 이상이 될 때까지 반복
	a = a + 1           # a += 1
	print('*' * a)
'''





## 문제 4. ##

'''
for a in range(1,101):
	print(a)
'''





## 문제 5. ##

'''
a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

result = 0

for Grade in a:
	result = result + Grade

ave = result / len(a)

print("합계 : ", result)
print("평균 : %0.2f" %ave)
'''




## 문제 6. ##

'''
num = [1, 2, 3, 4, 5]

result = []
for n in num:
	if n % 2 == 1:                  # n을 2로 나누었을 때 나머지가 1이면
		result.append( n * 2 )      # result에 n * 2한 값을 추가(append)해준다.

print(result)
'''