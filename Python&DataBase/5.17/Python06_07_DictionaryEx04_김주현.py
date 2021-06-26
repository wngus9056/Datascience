

a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
print(a.keys())

for x in a.keys():
	print(x)
print('-'*15)

xList = list(a.keys())
print(xList)
print('-'*15)

for y in range(3):
	print(xList[y])