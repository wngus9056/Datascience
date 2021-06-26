
# coding: utf-8

# Pandas05_12_DataFilterDoit05Rnage_김주현

# In[1]:


import pandas


# In[3]:


df = pandas.read_csv('./data/data/gapminder.tsv',sep='\t')


# In[4]:


s_range = list(range(5))
print(s_range)
print(type(s_range))


# In[5]:


df.head(3)


# In[6]:


subset = df.iloc[:, s_range]
print(subset.head(3))


# In[7]:


ss_range = list(range(3,6))
print(ss_range)


# In[8]:


subset1 = df.iloc[:, ss_range]
print(subset1.head(3))


# In[9]:


sss_range = list(range(0, 6, 2))
subset2 = df.iloc[:, sss_range]
print(subset2.head(3))

