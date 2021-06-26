
# coding: utf-8

# Pandas07_04_SeriesChk02Doit_김주현

# In[1]:


import pandas


# In[2]:


sr = pandas.Series(['banana', 42])
print(sr)


# In[3]:


sr1 = pandas.Series(['Wes McKinney', 'Creator of Pandas'])
print(sr1)


# In[4]:


sr2 = pandas.Series(['Wes McKinney', 'Creator of Pandas'], index = ('Person', 'Who'))
print(sr2)

