

# 다른 주석 값에 넣어보기.

a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a, '\t', b)


a = [1, 2, 3]
b = a
a[1] = 4
print(a, '\t', b)



from copy import copy
c = [1, 2, 3]
d = copy(c)
print(d)
print(id(c))
print(id(d))
