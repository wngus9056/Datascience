
# coding: utf-8

# Pandas06_12_InsaDBPractice01_김주현

# In[1]:


import pandas


# In[15]:


deptDB = pandas.read_csv('./data/data/sawonDB/deptDB.csv',names = ['deptno', 'dname', 'loc'], header = None)
sawonDB = pandas.read_csv('./data/data/sawonDB/sawonDB.csv', names = ['sabun', 'saname', 'deptno', 'sajob', 'sapay', 'sahire', 'sasex', 'samgr'], header = None)
gogekDB = pandas.read_csv('./data/data/sawonDB/gogekDB.csv', names = ['gobun', 'goname', 'gotel', 'gojumin', 'godam'], header = None)


# In[19]:


print(deptDB)
print('-'*30)
print(sawonDB)
print('-'*30)
print(gogekDB)

