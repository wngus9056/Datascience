
# coding: utf-8

# Pandas06_06_GroupByMulti01_김주현

# In[1]:


import pandas


# In[2]:


df = pandas.read_csv('./data/data/gapminder.tsv',sep='\t')


# In[8]:


mg = df.groupby(['year', 'continent'])['lifeExp']
print(mg)
print('='*60)
print(mg.mean())
print('='*60)
print(mg.mean().count())


# In[10]:


mg1 = df.groupby(['continent', 'year'])['lifeExp']
print(mg1)
print('='*60)
print(mg1.mean())
print('='*60)
print(mg1.mean().count())

