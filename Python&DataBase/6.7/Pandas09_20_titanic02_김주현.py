
# coding: utf-8

# In[1]:


import pandas
import seaborn


# In[2]:


titanic = seaborn.load_dataset('titanic')


# In[3]:


titanic['survived'].unique()


# In[4]:


titanic['sex'].unique()


# In[6]:


sur_cnt = titanic[titanic['survived'] == 1]
print('=====생존=====')
sur_cnt.groupby('sex')['survived'].count()


# In[8]:


die_cnt = titanic[titanic['survived'] == 0]
print('=====사망=====')
die_cnt.groupby('sex')['survived'].count()

