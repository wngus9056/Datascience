
# coding: utf-8

# Pandas05_08_DataFilterLifeExp_김주현

# In[2]:


import pandas


# In[5]:


df = pandas.read_csv('./data/data/gapminder.tsv', sep='\t')


# In[7]:


print(df.head())


# In[15]:


print(max(df['lifeExp'])) #최대수명
print(min(df['lifeExp'])) #최소수명

print('='*15)

print(max(df.loc[:,'lifeExp'])) #최대수명
print(min(df.loc[:, 'lifeExp'])) #최소수명

print('='*15)

print(max(df.iloc[:len(df)+1, 3])) #최대수명
print(min(df.iloc[:len(df)+1, 3])) #최소수명

