a = [1, 2, 3, 4]
result = []
for num in a:                   # a값을 num에 하나씩 저장시켜주고
	result.append(num*3)        # result변수에 저장받은 num * 3값을 추가(append)해준다.
print(result)
print('-' * 30)

result = [num*3 for num in a]   # result 변수에 (for문을 돌며 a값을 하나씩 num에 넣어주고 num * 3해준다.)
print(result)