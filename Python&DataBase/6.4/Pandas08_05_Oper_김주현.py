
# coding: utf-8

# Pandas08_05_Oper_김주현

# In[1]:


import pandas


# In[2]:


sc = pandas.read_csv('./data/data/scientists.csv')


# In[4]:


age = sc['Age']
print(age)


# In[6]:


print(age + age)
print('='*30)
print(age * age)
print('='*30)
print(age * 2)
print('='*30)
print(pandas.Series([1,100]))


# In[7]:


print(age + pandas.Series([1,100]))


# In[8]:


re_age = age.sort_index(ascending = False)
print(re_age)


# In[10]:


print(age)


# In[11]:


print(age + re_age)

