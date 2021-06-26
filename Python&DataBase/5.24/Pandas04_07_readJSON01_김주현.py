
# coding: utf-8

# Pandas04_07_readJSON01_김주현

# In[1]:


import pandas


# In[7]:


df = pandas.read_json('./DataSet/read_json_sample.json')


# In[8]:


print(df, '\n')
print(df.index)

