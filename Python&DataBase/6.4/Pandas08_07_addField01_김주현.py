
# coding: utf-8

# Pandas08_07_addField01_김주현

# In[2]:


import pandas


# In[3]:


sc = pandas.read_csv('./data/data/scientists.csv')


# In[4]:


print(sc['Born'].dtype)
print(sc['Died'].dtype)


# In[13]:


born_date = pandas.to_datetime(sc['Born'], format = '%Y-%m-%d')
died_date = pandas.to_datetime(sc['Died'], format = '%Y-%m-%d')


# In[15]:


print(born_date)
print('-'*20)
print(died_date)


# In[16]:


sc['born_dt'], sc['died_dt'] = (born_date, died_date)


# In[19]:


print(sc.head(3))
print('-'*20)
print(sc.shape)


# In[20]:


sc['age_days_dt'] = (sc['died_dt'] - sc['born_dt'])


# In[21]:


print(sc)

