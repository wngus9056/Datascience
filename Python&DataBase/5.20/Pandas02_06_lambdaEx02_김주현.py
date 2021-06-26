
# coding: utf-8

# Pandas02_06_lambdaEx02_김주현

# In[2]:


# lambda 활용법


# In[4]:


x = lambda a : a+10
print(x(7))


# In[5]:


x = lambda a,b : a+b
print(x(6,3))


# In[6]:


def myfunc(n):
    return lambda a: a*n


# In[7]:


mydoubler = myfunc(2)
print(mydoubler(10))


# In[8]:


def myfunc(n):
    return lambda a: a*n


# In[9]:


mytripler = myfunc(3)
print(mytripler(10))

