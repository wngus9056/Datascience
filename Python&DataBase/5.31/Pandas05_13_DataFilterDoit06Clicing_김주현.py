
# coding: utf-8

# Pandas05_13_DataFilterDoit06Clicing_김주현

# In[1]:


import pandas


# In[2]:


df = pandas.read_csv('./data/data/gapminder.tsv',sep='\t')


# In[4]:


subset = df.iloc[:, :3]
print(subset.head(3))
print('='*15)
subset1 = df.iloc[:, 0:6:2]
print(subset.head(3))


# In[7]:


print(df.iloc[[0, 99, 999], [0, 3, 5]])
print('='*15)
print(df.loc[[0, 99, 999], ['country', 'lifeExp', 'gdpPercap']])
print('='*15)
print(df.loc[10:13, ['country', 'lifeExp', 'gdpPercap']])
print('='*15)
print(df.iloc[10:13, [0, 3, -1]])

