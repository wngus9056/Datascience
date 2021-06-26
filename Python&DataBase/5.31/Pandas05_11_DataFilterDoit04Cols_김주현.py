
# coding: utf-8

# Pandas05_11_DataFilterDoit04Cols_김주현

# In[1]:


import pandas


# In[2]:


df = pandas.read_csv('./data/data/gapminder.tsv',sep='\t')


# In[3]:


df.head(3)


# In[6]:


subset = df.loc[:, ['year', 'pop']]
print(subset.head(3))
print('='*15)
subset1 = df.iloc[:, [2, 4, -1]]
print(subset1.head(3))

