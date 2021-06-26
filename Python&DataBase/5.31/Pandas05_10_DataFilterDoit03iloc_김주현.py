
# coding: utf-8

# 01_Pandas05_10_DataFilterDoit03iloc_김주현

# In[1]:


import pandas


# In[2]:


df = pandas.read_csv('./data/data/gapminder.tsv',sep='\t')


# In[3]:


print(df.head(3))


# In[4]:


print(df.iloc[1])


# In[5]:


print(df.iloc[99])


# In[6]:


print(df.iloc[-1])


# In[7]:


print(df.tail(1))
print(df.iloc[1703])
print(df.shape)


# In[8]:


print(df.iloc[[0, 99, 999]])

