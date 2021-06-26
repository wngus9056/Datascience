
# coding: utf-8

# Pandas08_03_DataFrameOper01_김주현

# In[1]:


import pandas
import seaborn


# In[2]:


titanic = seaborn.load_dataset('titanic')


# In[3]:


print(titanic.columns, '\n', titanic.shape)


# In[4]:


df = titanic.loc[:, ['age', 'fare']]


# In[5]:


print(df.head())
print('-'*20)
print(type(df))


# In[6]:


add = df + 10


# In[7]:


print(add.head())
print('-'*20)
print(type(add))


# In[8]:


sub = add - df


# In[9]:


print(sub.tail())
print('-'*20)
print(type(sub))


# In[13]:


test1 = pandas.DataFrame({'a' : [1, 2, 3], 'b' : [3, 4, 5]})
print(test1.shape)


# In[15]:


test_sum = df + test1
print(test_sum)

