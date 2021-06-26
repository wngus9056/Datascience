
# coding: utf-8

# Pandas06_04_GroupByChkPop_김주현

# In[1]:


import pandas


# In[2]:


df = pandas.read_csv('./data/data/gapminder.tsv',sep='\t')


# In[34]:


unilist = df['year'].unique()
print(unilist)


# In[39]:


for idx in unilist:
    yearlist = df[df['year'] == idx]
    print(yearlist['pop'].mean())

