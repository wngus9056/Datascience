
# coding: utf-8

# Pandas08_11_to_scv_김주현

# In[1]:


import pandas


# In[2]:


data = {'name' : ['Jerry', 'Rial', 'Paul'],       'algol' : ['A', 'A+', 'B'],       'basic' : ['C', 'B', 'B+'],       'c++' : ['B+', 'C', 'C+']}

df = pandas.DataFrame(data)
df.set_index('name', inplace = True)


# In[3]:


print(df)


# In[4]:


df.to_csv('./../df_sample.csv')

