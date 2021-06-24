list01 = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
print(len(list01))

sum = 0
for Grade in list01:
	sum = sum + Grade   # sum += Grade

ave = sum / len(list01) # len(list)는 list안의 값 개수를 출력한다.

print("합계 : ", sum)
print("평균 : %0.2f" %ave)