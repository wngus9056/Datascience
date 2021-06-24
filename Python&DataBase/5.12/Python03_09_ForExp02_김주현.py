a = [1, 2, 3, 4]

result = [num*3 for num in a if num % 2 ==0]   # result 변수에 (for문을 돌며 a값을 하나씩 num에 넣어주고 num을 2로 나눈 나머지가 0이면 num * 3)을 저장한다.
print(result)