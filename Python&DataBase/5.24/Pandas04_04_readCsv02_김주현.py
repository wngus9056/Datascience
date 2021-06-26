
# coding: utf-8

# Pandas04_04_readCsv02_김주현

# In[11]:


import pandas as pd


# In[12]:


a = pd.read_csv('./DataSet/read_csv_sample.csv')


# In[13]:


print(a)


# In[14]:


print(type(a))


# In[15]:


# file_path = ('C:/Study/Pandas_Work/DataSet/read_csv_sample.csv')


# In[16]:


# b = pandas.read_csv(file_path)


# In[17]:


# print(b)


# In[18]:


# print(type(b))


# In[19]:


df1 = pd.read_csv('./DataSet/read_csv_sample.csv', header = None)
print(df1)


# In[20]:


df2 = pd.read_csv('./DataSet/read_csv_sample.csv', index_col = None)
print(df2)


# In[21]:


df3 = pd.read_csv('./DataSet/read_csv_sample.csv', index_col = 'c0')
print(df3)


# In[28]:


df4 = pd.read_csv('./DataSet/read_csv_sample.csv', index_col = 'c2')
print(df4)

