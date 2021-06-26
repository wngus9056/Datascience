
# coding: utf-8

# In[1]:


import pandas
import seaborn


# In[2]:


titanic = seaborn.load_dataset('titanic')


# In[3]:


titanic.head(3)


# In[6]:


print(titanic.head(3))
print('-'*30)
print(titanic.tail(3))
print('-'*30)
print(titanic.shape)
print('-'*30)
print(titanic.info())
print('-'*30)


# In[7]:


print(titanic.columns)
print('-'*30)
print(len(titanic.columns))


# In[12]:


for idx in titanic.columns:
    print('[ {} ]'.format(idx))
    print(titanic[idx].unique())
    print('-'*30)

