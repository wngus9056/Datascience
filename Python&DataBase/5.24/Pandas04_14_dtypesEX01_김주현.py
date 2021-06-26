
# coding: utf-8

# Pandas04_14_dtypesEX01_김주현

# In[1]:


import pandas as pd


# In[8]:


df01 = pd.DataFrame({'float' : [1.0], 'int': [1],                      'datetime' : [pd.Timestamp('20210524')], 'string' : ['foo']})


# In[9]:


print(type(df01))


# In[10]:


df01.dtypes

