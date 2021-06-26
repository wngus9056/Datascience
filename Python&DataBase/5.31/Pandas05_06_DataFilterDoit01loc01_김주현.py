
# coding: utf-8

# Pandas05_06_DataFilterDoit01loc01_김주현

# In[1]:


import pandas


# In[2]:


df = pandas.read_csv('./data/data/gapminder.tsv', sep='\t')


# In[3]:


df.head(3)


# In[4]:


df.shape


# In[6]:


loc0 = df.loc[0]
print(loc0)
print(type(loc0))


# In[8]:


df.loc[85:100]


# In[9]:


print(df.loc[99])


# In[10]:


df.tail(3)


# In[11]:


# print(df.loc[-1])


# In[12]:


len(df)

