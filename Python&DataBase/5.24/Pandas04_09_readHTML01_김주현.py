
# coding: utf-8

# Pandas04_09_readHTML01_김주현

# In[1]:


import pandas as pd


# In[2]:


url = './DataSet/Pandas04_08_Test01_김주현.html'
df1 = pd.read_html(url)


# In[5]:


print(len(df1), '\n==>')


# In[6]:


print(df1, '\n==>')


# In[8]:


for i in range(len(df1)):
    print('tables[%s]' %i, '\n')
    print(df1[i], '\n')


# In[9]:


df2 = df1[0]
df3 = df1[1]


# In[11]:


print(df2.columns, '\n')


# In[12]:


print(df3.columns, '\n')

