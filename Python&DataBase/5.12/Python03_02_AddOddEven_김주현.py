add = 0
for a in range(11):
	add = add + a               # 반복문을 돌며 0부터 10까지 합을 구한다...add += a 와 같다.
print("1부터 10까지의 합: ",add)


odd = 0
for b in range(1,11,2):         # 반복문을 돌며 1부터 2씩 건너띄므로 홀수만 b에 저장된다...odd += b 와 같다.
	odd = odd + b
print("1부터 10까지의 홀수의 합: ", odd)

edd = 0                         # 반복문을 돌며 0부터 2씩 건너띄므로 짝수만 c에 저장된다...edd += c 와 같다.
for c in range(0,11,2):
	edd = edd + c
print("1부터 10까지의 짝수의 합: ", edd)