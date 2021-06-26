
# coding: utf-8

# Pandas05_04_DataFilterRows01Loc02_김주현

# In[1]:


import pandas


# In[6]:


df = pandas.DataFrame([[1, 2], [4, 5], [7, 8]],
    index = ['cobra', 'viper', 'sidewinder'],
    columns = ['max_speed', 'shield'])
df


# In[19]:


df.loc[['viper', 'sidewinder'], ['shield']] = 50
df


# In[20]:


df.loc['cobra'] = 10
df


# In[22]:


df.loc[:, 'max_speed'] = 30
df


# In[23]:


df.loc[df['shield'] > 35] = 0
df


# In[24]:


df1 = pandas.DataFrame([[1, 2], [4, 5], [7, 8]],
    index = [7, 8, 9],
    columns = ['max_speed', 'shield'])
df1


# In[25]:


df1.loc[7:9]

