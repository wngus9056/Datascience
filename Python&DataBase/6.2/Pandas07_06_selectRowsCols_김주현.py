
# coding: utf-8

# In[13]:


Pandas07_06_selectRowsCols_김주현


# In[1]:


import pandas


# In[4]:


ed = {'수학' : [90, 80, 70], '영어' : [98, 89, 95], '음악' : [85, 95, 100],     '체육' : [100, 90, 90]}

df = pandas.DataFrame(ed, index = ['서준', '우현', '인아'])
print(df, '\n')


# In[5]:


label1 = df.loc['서준']
position1 = df.iloc[0]
print(label1, '\n')
print(position1, '\n')


# In[6]:


label2 = df.loc[['서준', '우현']]
position2 = df.iloc[[0, 1]]
print(label1, '\n')
print(position2, '\n')


# In[7]:


label3 = df.loc['서준':'우현']
position3 = df.iloc[0:1]
print(label3, '\n')
print(position3)


# In[8]:


ed1 = {'이름' : ['서준', '우현', '인아'],      '수학' : [90, 80, 70], '영어' : [98, 89, 95],      '음악' : [85, 95, 100], '체육' : [100, 90, 90]}
df = pandas.DataFrame(ed1)
print(df, '\n')
print(type(df), '\n')


# In[11]:


math1 = df['수학']
print(math1, '\n')
print(type(math1), '\n')
print('='*30)
english = df.영어
print(english, '\n')
print(type(english), '\n')


# In[12]:


mg = df[['음악', '체육', ]]
print(mg, '\n')
print(type(mg), '\n')
print('='*30)
math2 = df[['수학']]
print(math2, '\n')
print(type(math2))
print('='*30)
math2 = df['수학']
print(math2, '\n')
print(type(math2))

