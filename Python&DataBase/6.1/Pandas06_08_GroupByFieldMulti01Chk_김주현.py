
# coding: utf-8

# Pandas06_08_GroupByFieldMulti01Chk_김주현

# In[11]:


import pandas


# In[100]:


df = pandas.read_csv('./data/data/gapminder.tsv',sep='\t')


# In[118]:


mg = df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']]
print(mg.mean())


# In[119]:


yeardf = df['year'].unique()
continentdf = df['continent'].unique()
print(yeardf)
print(continentdf)


# In[121]:


for a in yeardf:
    a1 = df[df['year'] == a]
    for b in continentdf:
        a2 = a1[df['continent'] == b]
        print(a, b, '\t',a2[['lifeExp','gdpPercap']].mean())
    print('-'*60)

