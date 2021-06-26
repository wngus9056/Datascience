

#리스트에 포함된 요소 x의 개수 세기(count)
a = [1, 5, 8, 4, 8, 4, 8, 8, 8, 5, 3, 4, 5, 6]
print(a.count(8))
print('-' * 15)

'''
리스트 확장(extend)
extend(x) 에서 x에는 리스트만 올 수 있으며 원래의 a리스트에 x리스트를 더한다.
'''

a = [1, 2, 3]
a.extend(['hi', 'Python'])
print(a)
print('-' * 15)
