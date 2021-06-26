
# coding: utf-8

# Pandas04_10_readTSV01_김주현

# In[11]:


import pandas


# In[12]:


df1 = pandas.read_csv('./data/data/gapminder.tsv', sep='\t')
print(df1)

