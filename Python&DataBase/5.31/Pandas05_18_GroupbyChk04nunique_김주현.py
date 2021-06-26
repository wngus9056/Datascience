
# coding: utf-8

# Pandas05_18_GroupbyChk04nunique_김주현

# In[1]:


import pandas


# In[2]:


df = pandas.read_csv('./data/data/gapminder.tsv',sep='\t')


# In[4]:


print(df.groupby('continent')['year'].nunique(), '\n=====>')
print(df.groupby('continent')['year'].unique(), '\n=====>')
print(df.groupby('continent')['year'].unique()['Asia'], '\n=====>')

