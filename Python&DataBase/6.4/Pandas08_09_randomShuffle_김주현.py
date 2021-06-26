
# coding: utf-8

# Pandas08_09_randomShuffle_김주현

# In[3]:


import random
import pandas


# In[4]:


sc = pandas.read_csv('./data/data/scientists.csv')


# In[34]:


random.seed(42)
random.shuffle(sc['Age'])
print(sc['Age'])

