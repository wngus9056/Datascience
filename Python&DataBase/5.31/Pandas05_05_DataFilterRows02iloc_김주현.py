
# coding: utf-8

# Pandas05_05_DataFilterRows02iloc_김주현

# In[2]:


import pandas


# In[3]:


mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
          {'a': 100, 'b': 200, 'c': 300, 'd': 400},
          {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000 }]
df = pandas.DataFrame(mydict)
df


# In[6]:


print(type(df.iloc[0]))


# In[7]:


print(type(df.iloc[[0]]))


# In[10]:


print(df.iloc[0])
print('='*15)
print(df.iloc[[0]])


# In[13]:


print(df.iloc[[0, 1]])
print('='*15)
print(df.iloc[0, 1])


# In[16]:


df.iloc[1:2]


# In[18]:


df.iloc[[True, False, True]]


# In[19]:


df.iloc[[1, 2], [2, 3]]


# In[24]:


df.iloc[1:3, 0:3]


# In[25]:


df.iloc[:, [True, True, False]]

