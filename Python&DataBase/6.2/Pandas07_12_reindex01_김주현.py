
# coding: utf-8

# Pandas07_12_reindex01_김주현

# In[1]:


import pandas


# In[2]:


dic = {'c0' : [1, 2, 3], 'c1' : [4, 5, 6], 'c2' : [7, 8, 9],      'c3' : [10, 11, 12], 'c4' : [13, 14, 15]}

df = pandas.DataFrame(dic)
print(df)


# In[3]:


df = pandas.DataFrame(dic, index = ['r0', 'r1', 'r2'])
print(df)


# In[5]:


new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf = df.reindex(new_index)
print(ndf)


# In[6]:


ndf = df.reindex(new_index, fill_value = 0)
print(ndf)

