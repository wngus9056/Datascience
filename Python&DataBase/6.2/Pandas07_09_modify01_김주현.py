
# coding: utf-8

# Pandas07_09_modify01_김주현

# In[1]:


import pandas


# In[2]:


ed1 = {'이름' : ['서준', '우현', '인아'],      '수학' : [90, 80, 70], '영어' : [98, 89, 95],      '음악' : [85, 95, 100], '체육' : [100, 90, 90]}
df = pandas.DataFrame(ed1)
print(df, '\n')


# In[3]:


df.set_index('이름', inplace = True)
print(df,'\n')


# In[5]:


df.iloc[0][3] = 80
print(df)


# In[6]:


df.loc['서준', '체육'] = 90
print(df)


# In[7]:


df.loc['서준']['체육'] = 100
print(df)

