
# coding: utf-8

# Pandas07_01_SeriesChk01_김주현

# In[1]:


import pandas


# In[3]:


# 리스트를 시리즈로 변환하여 변수 sr에 저장

list_data = ['2021-05-19', 3.14, 'ABC', 100, True]
sr = pandas.Series(list_data)
print(sr, '\n')


# In[4]:


# 인덱스 배열을 변수 idx에 저장. 데이터 값 배열은 변수 val에 저장
idx = sr.index
val = sr.values
print('sr.index : ', idx, '\n')
print('sr.index type : ', type(idx), '\n')
print('sr.values : ', val)
print('sr.index : ', type(val))


# In[6]:


# 튜플을 시리즈로 변환(인덱스 옵션에 인덱스 이름을 지정)
tup_data = ('영인', '2010-05-01', '여',True)

# sr = pandas.Series(tup_data)
sr = pandas.Series(tup_data, index = ['이름', '생년월일', '성별', '학생여부'])

print(sr, '\n')

# 원소를 1개 선택
print(sr[0], '\n')
print(sr['이름'])


# In[7]:


# 여러 개의 원소를 선택 (인덱스 리스트 활용)
print(sr[[1,2]], '\n')
print(sr[['생년월일', '성별']], '\n')

# 여러 개의 원소를 선택 (인덱스 범위 지정)
print(sr[1:2], '\n')
print(sr['생년월일' : '성별'])


# In[8]:


a = range(1, 7)
print(a)
for idx in a:
    print(idx)


# In[9]:


test = sr['생년월일' : '성별']
print(test)
type(test)

