
# coding: utf-8

# Pandas07_07_SeriesRowsCols2_김주현

# In[6]:


import pandas


# In[21]:


ed1 = {'이름' : ['서준', '우현', '인아'],      '수학' : [90, 80, 70], '영어' : [98, 89, 95],      '음악' : [85, 95, 100], '체육' : [100, 90, 90]}
df = pandas.DataFrame(ed1)
print(df, '\n')

df.set_index('이름', inplace = True)
print(df, '\n')

a = df.loc['서준', '음악']
print(a, '\b')
b = df.iloc[0, 2]
print(b, '\n')


# In[22]:


c = df.loc['서준', ['음악', '체육']]
print(c, '\n')
d = df.iloc[0, [2, 3]]
print(d, '\n')
e = df.loc['서준', '음악':'체육']
print(e)
f = df.iloc[0, 2:]
print(f, '\n')


# In[23]:


g = df.loc[['서준', '우현'], ['음악', '체육']]
print(g, '\n')
h = df.iloc[[0, 1], [2, 3]]
print('df.iloc[[0, 1], [2, 3]]\n', h, '\n')
i = df.loc['서준':'우현', '음악':'체육']
print('df.loc["서준":"우현", "음악":"체육"]\n', i, '\n')
j = df.iloc[0:2, 2:]
print(j)


# In[24]:


df.loc[:,['음악', '체육']]


# In[25]:


print(df)
df.iloc[:, [2, 3]]


# In[26]:


df.iloc[:, 2:4]

