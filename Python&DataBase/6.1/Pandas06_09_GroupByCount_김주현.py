
# coding: utf-8

# Pandas06_09_GroupByCount_김주현

# In[1]:


import pandas


# In[2]:


df = pandas.read_csv('./data/data/gapminder.tsv',sep='\t')


# In[4]:


print(df.groupby('continent')['country'])
print('='*60)
print(df.groupby('continent')['country'].nunique())
print('='*60)
print(df.groupby('continent')['country'].unique())
print('='*60)
print(df.groupby('continent')['country'].unique()['Oceania'])
print('='*60)
print(df.groupby('continent')['country'].count())
print('='*60)
print(df.groupby('continent')['country'].count()['Africa'])
print('='*60)

