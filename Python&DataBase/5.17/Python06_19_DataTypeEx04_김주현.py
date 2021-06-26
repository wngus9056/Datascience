

a = [1, 2, 3]
b = a

print('a, b 변경전 = ', a, "/", b)
a[1] = 4
print('a[1] 변경후 = ', a, "/", b)



c = [1, 2, 3]
d = [1, 2, 3]
print(id(c))
print(id(d))
c = d
print(id(c))
print(id(d))