
# coding: utf-8

# HW_Pandas09_PracticeChk02_김주현

# In[1]:


import pandas
import numpy


# In[2]:


s = pandas.Series(['1. Ant. ', '2. Bee!\n', '3. Cat?\t', numpy.nan])


# In[3]:


s


# In[4]:


s.str.strip()


# In[5]:


s.str.strip('.')


# In[6]:


s.str.strip('123.!? \n\t')


# In[9]:


s.str.lstrip('123.')


# In[11]:


s.str.rstrip('.!? \n\t')

