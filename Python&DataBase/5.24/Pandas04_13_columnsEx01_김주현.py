
# coding: utf-8

# Pandas04_13_columnsEx01_김주현

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('./data/data/gapminder.tsv', sep='\t')


# In[3]:


df.shape


# In[5]:


df.columns

