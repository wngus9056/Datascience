a = "{1:<10}".format('aa', 'bb', 'cc') # {n:<10} 에서 n은 format에서 가져올 인덱스이고 <는 왼쪽에 정렬하고 오른쪽에 값을 포함한 10칸을 만든다.
b = "{2:>10}".format('aa', 'bb', 'cc')
c = "{0:^10}".format('aa', 'bb', 'cc')  # 값을 가운데 정렬하고 값을 포함한 10칸을 만든다.
d = "{1:a^10}".format('aa', 'bb', 'cc') # {1:a^10}에서 a는 만드는 공백을 a로 채우라는 뜻이다.

print(a)
print(b)
print(c)
print(d)

x = 354899516
y = 154.288456

e1 = "{1:0.5f} {0:,d}".format(x,y)
e2 = "{1:20.3f}".format(x,y)

print(e1)
print(e2)