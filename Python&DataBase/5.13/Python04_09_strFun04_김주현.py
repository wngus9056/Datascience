a = " hi "
print(a)
print(a.lstrip()+'WOW') # ' hi '의 왼쪽 공백을 제거하고 'WOW'를 붙인다.
print(a.rstrip()+'WOW') # ' hi '의 오른쪽 공백을 제거한다.
print(a.strip()+'WOW')  # ' hi '의 양쪽 공백을 제거한다.
print('-'*15)

b = 'Life is too short'
print(b)
change = b.replace('Life', 'Your leg')  # change변수에 b변수에서 'Life'를 'Your leg'로 바꾼 값을 저장한다.
print(change)
print('-'*15)