
# coding: utf-8

# Pandas04_18_dataLookEx01_김주현

# In[1]:


import pandas as pd
df = pd.read_csv('./data/data/gapminder.tsv', sep='\t')


# In[2]:


# 데이터의 자료형을 확인
type(df)


# In[3]:


# 데이터프레임 열 확인
print(df.columns)


# In[4]:


# 데이터프레임 행 확인
df.index


# In[5]:


# 데이터프레임을 구성하는 값의 자료형 확인
print(df.dtypes)


# In[6]:


# 데이터 집합과 각 열들의 자료형을 자세히 확인
print(df.info())


# In[7]:


# (행, 열) 크기 확인
df.shape

