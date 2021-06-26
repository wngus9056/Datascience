
# coding: utf-8

# Pandas08_10_dropColumn_김주현

# In[1]:


import pandas


# In[4]:


sc = pandas.read_csv('./data/data/scientists.csv')


# In[5]:


print(sc.columns)


# In[6]:


sc_drop = sc.drop(['Age'], axis = 1)

print(sc_drop.columns)

