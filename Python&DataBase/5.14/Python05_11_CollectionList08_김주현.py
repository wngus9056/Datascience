

#리스트 요소 제거(remove)_첫 번째 3만 제거

a= [1, 2, 3, 1, 2, 3]
result01 = a.remove(3)
print(a)
print(result01)
print('-' * 15)

b = [1, 2, 3, 4, 5, 6]
result02 = b.pop()
print(b)
print(result02)
print('-' * 15)

c = [1, 2, 3]
result03 = c.pop(2)
print(c)
print(result03)
print('-' * 15)