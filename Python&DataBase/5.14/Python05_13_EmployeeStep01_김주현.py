

# 인사 관리 시스템

TName = ["구분","사원명","입사일","급여"]

empInfo = [
	['T160501',"캔디","2016-05-10"],
	['R160510',"장미","2016-05-10"],
	['t160811',"튤립","2016-08-15"],
	['T160821',"포도","2016-08-22"],
	['r160850',"사과","2016-08-30"]
]

empPayTable = [
	[250,10],
	[200,12],
	[300,9],
	[230,11],
	[150,12]
]



number = int(len(empInfo))

# T, t, R 추출하고 upper

name_check = []
for x in range(0, number):
	name01 = empInfo[x][0][0]
	name_check.append(name01)
#print(name_check)



name_upper = []
for i in name_check:
	name_upper.append(i.upper())
#print(name_upper)



name_final = []
for x in range(0,number):
	if name_upper[x] == 'T':
		name_final.append("계약직")
	if name_upper[x] == 'R':
		name_final.append("정규직")
#print(name_final)

# 이름 추출

name012 = []
for q in range(0, number):
	name011 = empInfo[q][1][:]
	name012.append(name011)
#print(name012)

# 입사일 추출

day01= []
for q in range(0, number):
	day011 = empInfo[q][2][:]
	day01.append(day011)
#print(day01)


# 급여추출 및 계산

pay = []
for w in range(0, number):
	pay01 = empPayTable[w][0]
	pay.append(pay01)
#print(pay)



pay2 = []
for w in range(0, number):
	pay02 = empPayTable[w][1]
	pay2.append(pay02)
#print(pay2)


paytotal = pay[0] * pay2[0]
total = []
for e in range(0, number):
	total01 = pay[e] * pay2[e]
	total.append(total01)
#print(total)



empPayTable


print(TName[0], '\t', TName[1], '\t', TName[2], '\t', TName[3])
print('=' * 46)
for y in range(0, number):
	print("%s\t %s\t\t%s\t %s" %(name_final[y], name012[y], day01[y], total[y]))






'''
print("-"*46)
print("%s\t%s\t%s\t%d" %(name_check, name02, day01, years))
'''
