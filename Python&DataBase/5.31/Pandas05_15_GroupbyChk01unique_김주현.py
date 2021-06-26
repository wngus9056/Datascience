
# coding: utf-8

# Pandas05_15_GroupbyChk01_김주현

# In[1]:


import pandas


# In[2]:


df = pandas.read_csv('./data/data/gapminder.tsv', sep='\t')


# In[6]:


print(df.groupby('year')['lifeExp'].mean())


# In[7]:


print(df['year'].unique())
print('='*15)
df['year'].unique()


# In[5]:


print(type(df['year'].unique()))

