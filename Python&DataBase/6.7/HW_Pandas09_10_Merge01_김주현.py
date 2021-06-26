
# coding: utf-8

# HW_Pandas09_10_Merge01_김주현

# In[1]:


import pandas


# In[11]:


df1 = pandas.DataFrame({'a' : ['foo', 'bar'], 'b' : [1, 2]})
df2 = pandas.DataFrame({'a' : ['foo', 'baz'], 'c' : [3, 4]})


# In[12]:


print(df1)
print('-'*15)
print(df2)


# In[13]:


#조건에 맞는 것만 합쳐서
df1.merge(df2, how = 'inner', on = 'a')


# In[14]:


#df1는 다 가져오고 df2는 조건에 맞게
df1.merge(df2, how = 'left', on = 'a')


# In[15]:


#df1은 조건에 맞게 df2는 다 가져와
df1.merge(df2, how = 'right', on = 'a')

