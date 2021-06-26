
# coding: utf-8

# Pandas07_02_DataFrameChk01_김주현

# In[1]:


import pandas


# In[2]:


# 열이름을 key로 하고, 리스트를 value로 갖는 딕셔너리 정의(2차 배열)

dic_data = {'c0' : [1, 2, 3], 'c1' : [4, 5, 6],             'c2' : [7, 8, 9], 'c3' : [10, 11, 12], 'c4' : [13, 14, 15]}


# In[3]:


# 판다스 DataFrame() 함수로 딕셔너리를 데이터프레임으로 변환, 변수 df에 저장

df = pandas.DataFrame(dic_data)


# In[4]:


# df의 자료형 출력

print(type(df), '\n')

# 변수 df에 저장되어 있는 데이터프레임 객체를 출력

print(df)


# In[11]:


# 행 인덱스/열 이름 지정하여, 데이터프레임 만들기

df1 = pandas.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],                      index = ['준서', '예은'],                      columns = ['나이', '성별', '학교'])

# 행 인덱스, 열 이름 확인하기

print(df1, '\n')
print(df1.index, '\n')
print(df1.columns, '\n')


# In[12]:


# 행 인덱스, 열 이름 변경하기

df1.index = ['학생1', '학생2']
df1.columns = ['연령', '남녀', '소속']

print(df1, '\n')
print(df1.index, '\n')
print(df1.columns, '\n')


# In[18]:


# 행 인덱스/열 이름 지정하여, 데이터프레임 만들기

df2 = pandas.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],                      index = ['준서', '예은'],                      columns = ['나이', '성별', '학교'])

# 데이터프레임 df 출력
print(df2, '\n')

redf = df2.rename(columns={'나이':'연령', '성별':'남녀', '학교':'소속'})
df2.rename(index={'준서':'학생1', '예은':'학생2'})


# In[17]:


# df 출력 (변경 후)

print(redf)
print(df2)
print('='*40)

df2.rename(columns={'나이':'연령', '성별':'남녀', '학교':'소속'}, inplace = True)
df2.rename(index={'준서':'학생1', '예은':'학생2'}, inplace = True)
print(df2)

