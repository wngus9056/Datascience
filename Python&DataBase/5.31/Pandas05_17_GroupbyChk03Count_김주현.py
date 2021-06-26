
# coding: utf-8

# Pandas05_17_GroupbyChk03Count_김주현

# In[1]:


import pandas


# In[2]:


df = pandas.read_csv('./data/data/gapminder.tsv',sep='\t')


# In[29]:


unilist = df.groupby('continent')['year'].count()
unilist1 = df['continent'].unique()


# In[36]:


for idx in unilist1:
    print(idx, '=====> 1. : ')
    grcon = df[df['continent'] == idx]
    print(len(grcon), '\n=====> 2 \n', grcon.head(3), '\n=====> 3 : ', grcon.shape)

