
# coding: utf-8

# Pandas04_11_headEx01_김주현

# In[1]:


import pandas as pd


# In[4]:


df = pd.DataFrame({'animal' : ['alligator', 'bee', 'falcon', 'lion', 'monkey',                                'parrot', 'shark', 'whale', 'zebra', 'cat']})


# In[7]:


print(df)


# In[6]:


print(df.head())


# In[8]:


print(df.head(2))


# In[9]:


print(df.head(-3))

