
# coding: utf-8

# HW_Pandas09_11_Merge02deptSawon_김주현

# In[1]:


import pandas


# In[2]:


deptDB = pandas.read_csv('./data/data/sawonDB/deptDB.csv',names = ['deptno', 'dname', 'loc'], header = None)
sawonDB = pandas.read_csv('./data/data/sawonDB/sawonDB.csv', names = ['sabun', 'saname', 'deptno', 'sajob', 'sapay', 'sahire', 'sasex', 'samgr'], header = None)
gogekDB = pandas.read_csv('./data/data/sawonDB/gogekDB.csv', names = ['gobun', 'goname', 'gotel', 'gojumin', 'godam'], header = None)


# In[3]:


# ' 전처리 후 저장
deptDB = deptDB.replace('\'','',regex=True)
sawonDB = sawonDB.replace('\'','',regex=True)
gogekDB = gogekDB.replace('\'','',regex=True)


# In[4]:


# 공백 전처리 후 저장
deptDB_str = deptDB.replace(' ', '', regex = True)
sawonDB_str = sawonDB.replace(' ', '', regex= True)
gogekDB_str = gogekDB.replace(' ', '', regex = True)


# In[8]:


desa = deptDB_str.merge(sawonDB_str, how = 'inner', on = 'deptno')
desa = desa.sort_values('sabun')
desa.head(10)

