
# coding: utf-8

# Pandas06_02_Statistic01BuiltIn_김주현

# In[2]:


import pandas


# In[3]:


num = [28, 31, 24, 25, 30, 32, 20, 30, 31, 26, 31]


# In[4]:


dt = pandas.Series(num)


# In[5]:


print('Built_in 정렬 : {}'.format(dt.sort_values(ascending=True)))
print('Built_in 평균 : {}'.format(dt.mean()))
print('Built_in 중위수 : {}'.format(dt.median()))
print('Built_in 분산 : {}'.format(dt.var()))
print('Built_in 표준편차 : {}'.format(dt.std()))
print('Built_in 제1사분위수 : {}'.format(dt.quantile(q=0.25)))
print('Built_in 제2사분위수 : {}'.format(dt.quantile(q=0.5)))
print('Built_in 제3사분위수 : {}'.format(dt.quantile(q=0.75)))

