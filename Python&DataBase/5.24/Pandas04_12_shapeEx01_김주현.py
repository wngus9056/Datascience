
# coding: utf-8

# Pandas04_12_shapeEx01_김주현

# In[1]:


import pandas as pd


# In[2]:


a = pd.DataFrame({'col1' : [1, 5, 8], 'col2' : [8, 4, 7]})


# In[3]:


a.shape


# In[4]:


b = pd.DataFrame({'col1' : [1, 5, 8], 'col2' : [8, 4, 7], 'col3' : [2, 4, 7]})


# In[5]:


print(b)


# In[6]:


b.shape

