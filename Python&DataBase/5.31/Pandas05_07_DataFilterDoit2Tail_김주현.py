
# coding: utf-8

# Pandas05_07_DataFilterDoit2Tail_김주현

# In[1]:


import pandas


# In[2]:


df = pandas.read_csv('./data/data/gapminder.tsv', sep='\t')


# In[3]:


number_of_rows = df.shape[0]
print(number_of_rows, '\n\n')


# In[5]:


last_row_index = number_of_rows - 1
print(df.loc[last_row_index])


# In[7]:


print(df.loc[last_row_index])


# In[8]:


print(df.loc[len(df)-1])


# In[11]:


print(df.loc[len(df)-1])


# In[12]:


print(df.tail(n=1))


# In[13]:


print(df.tail(n=2))


# In[14]:


print(df.loc[[0, 99, 999]])

