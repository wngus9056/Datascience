
# coding: utf-8

# Pandas06_07_GroupByMulti01Chk_김주현

# In[11]:


import pandas


# In[100]:


df = pandas.read_csv('./data/data/gapminder.tsv',sep='\t')


# In[101]:


yeardf = df['year'].unique()
continentdf = df['continent'].unique()
print(continentdf)


# In[108]:


for a in yeardf:
    a1 = df[df['year'] == a]
    for b in continentdf:
        a2 = a1[df['continent'] == b]
        print(a, b, '\t',a2['lifeExp'].mean())
    print('-'*60)

