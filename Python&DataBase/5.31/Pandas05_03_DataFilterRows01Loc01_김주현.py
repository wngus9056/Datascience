
# coding: utf-8

# Pandas05_03_DataFilterRows01Loc01_김주현

# In[1]:


import pandas


# In[6]:


df = pandas.DataFrame([[1, 2], [4, 5], [7, 8]],
    index = ['cobra', 'viper', 'sidewinder'],
    columns = ['max_speed', 'shield'])
df


# In[7]:


df.loc['viper']


# In[8]:


df.loc[0]


# In[11]:


df.loc[['viper', 'sidewinder']]


# In[12]:


df.loc['cobra', 'shield']


# In[13]:


df.loc['cobra' : 'viper', 'max_speed']


# In[14]:


df.loc[[False, True, True]]


# In[15]:


df.loc[df['shield'] > 5]


# In[16]:


df.loc[df['shield'] > 6, ['max_speed']]


# In[17]:


df.loc[df['max_speed'] > 3, ['shield']]

