
# coding: utf-8

# Pandas07_15_indexValueKeyDoit_김주현

# In[2]:


import pandas


# In[3]:


sc1 = pandas.DataFrame({'Name' : ['Rosaline Franklin', 'William Gosset'],                       'Occupation' : ['Chemist', 'Statistician'],                      'Born' : ['1920-07-25', '1876-06-13'],                      'Died' : ['1958-04-16', '1937-10-16'],                      'Age' : [37, 61]},
                      index = ['Rosaline Franklin', 'William Gosset'],
                      columns = ['Occupation', 'Born', 'Age', 'Died'])
print(sc1)


# In[5]:


fr = sc1.loc['William Gosset']
print(type(fr))
print('-'*30)
print(fr)


# In[6]:


print(fr.index)
print('='*30)
print(fr.values)
print('='*30)
print(fr.keys())
print('='*30)
print(fr.index[0])
print('='*30)
print(fr.keys()[0])


# In[7]:


ages = sc1['Age']
print(ages)


# In[8]:


print(ages.mean())
print('='*30)
print(ages.min())
print('='*30)
print(ages.max())
print('='*30)
print(ages.std())

