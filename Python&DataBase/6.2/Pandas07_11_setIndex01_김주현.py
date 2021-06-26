
# coding: utf-8

# Pandas07_11_setIndex01_김주현

# In[1]:


import pandas


# In[2]:


ed1 = {'이름' : ['서준', '우현', '인아'],      '수학' : [90, 80, 70], '영어' : [98, 89, 95],      '음악' : [85, 95, 100], '체육' : [100, 90, 90]}
df = pandas.DataFrame(ed1)
print(df, '\n')


# In[6]:


ndf = df.set_index(['이름'])
print(ndf)
print('-'*30)
ndf2 = ndf.set_index('음악')
print(ndf2)
print('-'*30)
ndf3 = ndf.set_index(['수학','음악'])
print(ndf3)
print('-'*30)
ndf4 = df.set_index(['음악', '체육'])
print(ndf4)

