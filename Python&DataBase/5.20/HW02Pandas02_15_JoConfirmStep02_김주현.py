
import random


while True:
	user_name = []
	number = []
	user_name = input('4인 이상의 이름을 입력하세요 : ').split()
	if len(user_name) < 4:
		print('^ 명수를 확인하세요.')
		continue
	elif len(user_name) >= 4:
		while True:
			num = random.randint(1,len(user_name))
			if num not in number:
				number.append(num)
			else:
				continue
			
			if len(number) == len(user_name):
				break
	for i in user_name:
		print(i, end='  ')
	print()
	for i in number:
		print(i, end='\t')
	print()




'''
def def_num4():
	while True:
		num = random.randint(1, len(a))
		if num not in b:
			b.append(num)
		else:
			continue
'''

'''
def def_under4():
	print('^ 명수를 확인하세요 ( 4인 이상 )')

def def_upper4():
	while True:
		number = random.randint(1, len(data_input))
		if number not in b:
			b.append(number)
		else:
			continue
		if len(str(b)) == len(str(number)):
			break


def def_bone():
	if len(data_input) < 4:
		def_under4()
	elif len(data_input) >= 4:
		def_upper4()


num_check = []
b = []

while True:
	data_input = input('4인 이상의 이름을 입력하세요 (스페이스바로 구분) : ').split( )
	def_bone()

print(data_input)
print(b)
'''

'''
number = []

while len(number) <3:
	num = random.randint(1,9)
	if num not in number:
		number.append(num)
print(number)
'''


