
# coding: utf-8

# Pandas05_14_uniqueChk01_김주현

# In[1]:


import pandas


# In[3]:


s = pandas.Series([1, 2, 3,4 , 5, 6, 7, 7, 7, 8, 9])


# In[7]:


print(s.unique())


# In[8]:


print(s.nunique())

