a = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=python'
e = a.split('?')    # e에 a변수를 '?' 기준으로 나눠서 저장한다.
b = a.replace('https://search.naver.com/search.naver?', '')
c = b.split('&')
print(e[0])
print('QueryString')

for x in range(0,len(c)):
	print(' ',c[x])
print("QueryString 개수는 : ", len(c), "개 입니다.")




'''
b = a.split('?')
print(b)

c= list(b)
print(c)

c.remove('https://search.naver.com/search.naver')
print(c)
'''
