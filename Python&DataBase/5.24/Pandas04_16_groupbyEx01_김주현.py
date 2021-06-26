
# coding: utf-8

# Pandas04_16_groupbyEx01_김주현

# In[1]:


import pandas as pd


# In[3]:


df = pd.DataFrame({'Animal' : ['Falcon', 'Falcon', 'Parrot', 'Parrot']                  , 'Max Speed' : [380, 370, 24, 26]})


# In[4]:


df.groupby(['Animal']).mean()


# In[5]:


df.groupby(['Animal']).sum()

