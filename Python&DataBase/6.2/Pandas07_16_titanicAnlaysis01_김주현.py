
# coding: utf-8

# Pandas07_16_titanicAnlaysis01_김주현

# In[1]:


import pandas
import seaborn


# In[4]:


titanic = seaborn.load_dataset('titanic')


# In[8]:


print(titanic.head(3))


# In[10]:


# 행렬 Chk
print(titanic.shape)


# In[7]:


# 컬럼명 Chk
print(titanic.columns)


# In[26]:


# 컬럼 유니크 값
for a in titanic.columns:
    print(a,'의 유니크 값 : ',titanic[a].unique())
    print('-'*90)


# In[13]:


# 나이 최소,최대
print('최소 나이는',titanic['age'].min(),'이고,', '최대 나이는',titanic['age'].max(),'입니다.')


# In[27]:


# 성별 survived 개수
print(titanic.groupby(['sex', 'survived'])['survived'].count())


# In[30]:


# 남자, 여자 명수
print(titanic.groupby('sex')['survived'].count())

