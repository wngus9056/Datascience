

a = [1, 2, 3, ['a', 'b', 'c']]

print(a[0])
print(a[-1])
print(a[3])
print('-' * 15)

print(a[-1][0])
print(a[-1][2])
print(a[3][0])
print(a[3][2])
print('-' * 15)

b = [1, 2, ['a', 'b', ['Life', 'is']]]

print(b[2][2][0] + b[2][2][1])