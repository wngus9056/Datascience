for i in range(2,10):
	print("# %d 단" % i, end='		')  # print end옵션으로 ''를 주면 반복문을 돌 때 기본 디폴트인 엔터 대신 옆으로 나열해준다
print()
print("="*120)



for x in range(1,10):       # x = 1                         x = 2                       ...
	for y in range(2,10):   # y = 2, 3, 4, 5, 6, 7, 8, 9    y = 2, 3, 4, 5, 6, 7, 8, 9  ...
		print("{} * {} = {}".format(y, x, x*y), end='\t')   # {} {} {} 하고 .format(값1, 값2, 값3) 포맷으로 준 값1, 값2, 값3이 차례대로 들어간다.
	print()                                                 # {3} {2} {1} .format (값1, 값2, 값3) 은 값3, 값2, 값1로 인덱스대로 들어간다.


print('-'*120)




'''
for x in range(2,10):
	for y in range(1,10):
		print(x ,"X", y, "=", x*y, end='\t')
	print()

print("-"*120)
'''



