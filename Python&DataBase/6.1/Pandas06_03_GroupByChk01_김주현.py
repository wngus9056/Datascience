
# coding: utf-8

# Pandas06_03_GroupByChk01_김주현

# In[1]:


import pandas


# In[2]:


df = pandas.read_csv('./data/data/gapminder.tsv',sep='\t')


# In[3]:


print(type(df))
print('='*30)
print(type(df['pop']))


# In[7]:


gryeardf = df.groupby('year')
print(type(gryeardf))
print('='*30)
print(gryeardf['pop'])

