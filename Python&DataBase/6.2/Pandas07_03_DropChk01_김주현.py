
# coding: utf-8

# Pandas07_03_DropChk01_김주현

# In[1]:


import pandas


# In[2]:


# DataFrae() 함수로 데이터프레임 변환, 변수 df에 저장

exam_data = {'수학' : [90, 80, 70], '영어' : [98, 89, 95],            '음악' : [85, 95, 100], '체육' : [100, 90, 90]}

df = pandas.DataFrame(exam_data)
print(df, '\n')

df = pandas.DataFrame(exam_data, index = ['서준', '우현', '인아'])
print(df, '\n')


# In[3]:


# 데이터프레임 df를 복제하여 변수 df2에 저장, df2의 1개 행(row)을 삭제
df2 = df[:]
df2.drop('우현', inplace = True)
print(df2, '\n')


# In[4]:


# 데이터프레임 df를 복제하여 변수 df3에 저장, df3의 2개 행(row)을 삭제
df3 = df[:]
df3.drop(['우현', '인아'], inplace = True)
print(df3, '\n')


# In[5]:


# 데이터프레임 df를 복제하여 변수 df4에 저장, df4의 1개 열(columns)을 삭제
df4 = df[:]
df4.drop('수학', axis = 1, inplace = True)
print(df4, '\n')


# In[6]:


# 데이터프레임 df를 복제하여 변수 df4에 저장, df4의 2개 열(columns)을 삭제
df5 = df[:]
df5.drop(['영어', '음악'], axis = 1, inplace = True)
print(df5)

