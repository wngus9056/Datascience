
# coding: utf-8

# Pandas08_06_OperDataFrame_김주현

# In[1]:


import pandas


# In[2]:


sc = pandas.read_csv('./data/data/scientists.csv')


# In[3]:


print(sc[sc['Age'] > sc['Age'].mean()])


# In[7]:


print(sc.loc[[True, True, True, False, False, True, False, True]])


# In[6]:


sc


# In[8]:


print(sc * 2)

