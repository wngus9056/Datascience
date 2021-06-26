
# coding: utf-8

# Pandas04_15_infoEx01_김주현

# In[1]:


import pandas as pd


# In[2]:


int_values = [1, 2, 3, 4, 5]
text_values = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
float_values = [0.0, 0.25, 0.5, 0.75, 1.0]
df = pd.DataFrame({'int_col' : int_values, 'text_col' : text_values,                  'float_col' : float_values})


# In[3]:


df


# In[5]:


df.dtypes


# In[8]:


df.info()


# In[9]:


df.info(verbose = True)


# In[7]:


df.info(verbose = False)

