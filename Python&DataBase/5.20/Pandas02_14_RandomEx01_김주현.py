

import random

print('랜덤으로 숫자 불러오기\n')

for x in range(5):
	print('%f' %random.random(), end='')

print('\n', '-'*46, '\n')

for x in range(5):
	print('%d' %random.randint(1,4), end='  ')

print('\n', '-'*46, '\n')

for x in range(5):
	print('%d' %random.randint(1,90), end='  ')

print('\n', '-'*46, '\n')
