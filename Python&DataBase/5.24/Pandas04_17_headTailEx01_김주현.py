
# coding: utf-8

# Pandas04_17_headTailEx01_김주현

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('./data/data/gapminder.tsv', sep='\t')


# In[3]:


print(df.shape)
print(df.shape[0])
print(df.shape[1])


# In[4]:


len(df)


# In[5]:


df.head()


# In[6]:


df[0:5]


# In[10]:


df.head(7)


# In[11]:


df.head(n=7)


# In[12]:


df.tail()


# In[13]:


df.tail(n=7)


# In[14]:


df[len(df)-14:len(df)+1]

