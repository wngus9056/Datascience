
# coding: utf-8

# Pandas09_14_ColumnSort01_김주현

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
deptDB_str = deptDB[:]
deptDB_str['dname'] = deptDB_str['dname'].str.strip()
deptDB_str['loc'] = deptDB_str['loc'].str.strip()
# deptDB_str.apply(lambda x: x.str.strip(), axis = 1)

sawonDB_str = sawonDB[:]
sawonDB_str['saname'] = sawonDB_str['saname'].str.strip()
sawonDB_str['sajob'] = sawonDB_str['sajob'].str.strip()
sawonDB_str['sahire'] = sawonDB_str['sahire'].str.strip()
sawonDB_str['sasex'] = sawonDB_str['sasex'].str.strip()
# sawonDB_str.apply(lambda x: x.str.strip(), axis = 1)

gogekDB_str = gogekDB[:]
gogekDB_str['goname'] = gogekDB_str['goname'].str.strip()
gogekDB_str['gotel'] = gogekDB_str['gotel'].str.strip()
gogekDB_str['gojumin'] = gogekDB_str['gojumin'].str.strip()
# gogekDB_str.apply(lambda x: x.str.strip(), axis = 1)


# In[5]:


# 컬럼기준으로 sort
col_sort = sawonDB_str.columns.sort_values()
print(col_sort)


# In[9]:


sawonDB_str[col_sort]


# In[10]:


# 사번기준으로 sort
sabun_sort = sawonDB_str.sort_values('sabun')


# In[12]:


sabun_sort

