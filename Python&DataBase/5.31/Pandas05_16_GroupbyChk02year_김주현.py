
# coding: utf-8

# Pandas05_16_GroupbyChk02year_김주현

# In[1]:


import pandas


# In[2]:


df = pandas.read_csv('./data/data/gapminder.tsv',sep='\t')


# In[3]:


unilist = df.groupby('year')['lifeExp'].mean()


# In[4]:


for idx in unilist:
    print(idx, '=====> 1 : ')
    gryear = df[df['year'] == idx]
    print(len(gryear), '\n=====> 2 \n', gryear.head(3), '\n=====> 3 : ', gryear.shape)
    print(gryear['lifeExp'].mean())


# In[5]:


print(df.groupby('year')['lifeExp'].mean())

