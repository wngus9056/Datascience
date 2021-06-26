
# coding: utf-8

# In[1]:


import pandas


# In[2]:


test = pandas.Series(['lama', 'cow', 'lama', 'beet', 'lama', 'cat', 'hippo'], name = 'Animal')


# In[3]:


test.isin(['cow', 'lama'])

