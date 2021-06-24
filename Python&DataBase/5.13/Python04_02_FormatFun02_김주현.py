a = "My name {}".format('Hong')             # format으로 주어진 값을 차례대로 가져온다.
b = "{0} x {1} = {2}".format(2, 11, 11*2)   # {}안에 입력한 숫자대로 format에서 인덱스값으로 가져온다.
c = "{b} x {c} = {a}".format (a= 11*2, b= 2, c= 11) # {}안에 변수로 주면 format에서 준 변수를 가져온다.

print(a)
print(b)
print(c)