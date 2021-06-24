a = 'Life is too short, You need Python'

print(a[3], a[0], a[12], a[-1], a[-0], a[-2], a[-5])
#ooooo
print(a[9], a[10], a[14], a[20], a[-2])

print(a[0:4])   # a의 인덱스 0부터 4까지 출력
print(a[0:2], a[5:7], a[12:17]) # a의 인덱스 0부터2, 5부터7, 12부터 17까지 출력
print(a[19:])   # 인덱스 19부터 끝까지 출력
print(a[:5])    # 인덱스 처음부터 5까지 출력
print(a[:])     # a 전체 출력
print(a[19:-7]) # a 인덱스 19부터 끝에서 7번째까지 출력