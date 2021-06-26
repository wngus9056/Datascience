
# coding: utf-8

# Pandas07_10_transpose01_김주현

# In[1]:


import pandas


# In[2]:


ed1 = {'이름' : ['서준', '우현', '인아'],      '수학' : [90, 80, 70], '영어' : [98, 89, 95],      '음악' : [85, 95, 100], '체육' : [100, 90, 90]}
df = pandas.DataFrame(ed1)
print(df, '\n')


# In[4]:


df = df.transpose()
print(df)


# In[5]:


df = df.T
print(df)

