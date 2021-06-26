

number = int(input("^10이상의 숫자를 입력해주세요. [ Exit : 0 ] : "))
fruit_name = ["Apple", "Melon", "Grape", "StrawBerry"]
fruit_num = [3, 4, 5, 8]
fruit_count = [0, 0, 0, 0]

print("==<< %d회 반복합니다. >>==" %number)

for x in range(1, number+1):
	print("\n%d. " %x, end='')
	for y in range(len(fruit_name)):
		if (x % fruit_num[y] == 0):
			fruit_count[y] += 1
			print("%s" %fruit_name[y], end = '')

print("\n\n==<< Fruit Count List >>==")
for i in range(len(fruit_name)):
	print("%d. %s %d회" %(i+1, fruit_name[i], fruit_count[i]))