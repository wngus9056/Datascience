
# coding: utf-8

# Pandas05_02_DataFilterCols01_김주현

# In[1]:


import pandas


# In[2]:


df = pandas.read_csv('./data/data/gapminder.tsv', sep='\t')


# In[3]:


country_df = df['country']


# In[4]:


print(type(country_df))


# In[5]:


print(country_df.head())


# In[6]:


print(country_df.tail())


# In[7]:


subset = df[['country', 'continent', 'year']]
print(type(subset))


# In[8]:


print(subset.head())


# In[9]:


print(subset.tail())


# In[10]:


print(subset[1700:len(subset)+1])

