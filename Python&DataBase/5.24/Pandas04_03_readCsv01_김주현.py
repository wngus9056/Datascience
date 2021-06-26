
# coding: utf-8

# Pandas04_03_readCsv01_김주현

# In[11]:


import pandas as pd


# In[12]:


a = pd.read_csv('./DataSet/read_csv_sample.csv')


# In[13]:


print(a)


# In[14]:


print(type(a))


# In[15]:


file_path = ('C:/Study/Pandas_Work/DataSet/read_csv_sample.csv')


# In[16]:


b = pandas.read_csv(file_path)


# In[17]:


print(b)


# In[18]:


print(type(b))

