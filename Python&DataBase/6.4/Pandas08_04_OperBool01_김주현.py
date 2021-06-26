
# coding: utf-8

# Pandas08_04_OperBool01_김주현

# In[1]:


import pandas


# In[2]:


sc = pandas.read_csv('./data/data/scientists.csv')


# In[3]:


age = sc['Age']


# In[5]:


print(age[age > age.mean()])


# In[6]:


print(age > age.mean())


# In[7]:


print(type(age > age.mean()))


# In[8]:


mvalues = [True, True, False, False, True, True, False, True]
print(age[mvalues])

