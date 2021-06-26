
# coding: utf-8

# Pandas06_05_GroupByContinentLifeExp_김주현

# In[1]:


import pandas


# In[3]:


df = pandas.read_csv('./data/data/gapminder.tsv',sep='\t')


# In[5]:


group_continent = df.groupby('continent')
print(group_continent['lifeExp'].mean())


# In[8]:


unilist = df['continent'].unique()
for idx in unilist:
    continentlist = df[df['continent'] == idx]
    print(idx+'의 기대수명 평균은 ',continentlist['lifeExp'].mean())

