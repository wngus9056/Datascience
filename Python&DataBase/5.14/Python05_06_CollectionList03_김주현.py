

a = [1, 2, 3, 4, 5]

print(a[0:2])
print(a[:2])
print(a[2:])

print('-'*15)

b = [1, 2, 3, ['a', 'b', 'c'], 4, 5]

print(b[2:5])
print(b[3][1:-1])
print(b[3][:])

print('-'*15)


c = [1, 2, 3, ['a', 'b', 'c', 'd', 'e'], 4, 5, 6, 7]

print(c[3][1:-2])