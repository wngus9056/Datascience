
# coding: utf-8

# Pandas09_12_Merge03dname_김주현

# In[1]:


import pandas


# In[2]:


deptDB = pandas.read_csv('./data/data/sawonDB/deptDB.csv',names = ['deptno', 'dname', 'loc'], header = None)
sawonDB = pandas.read_csv('./data/data/sawonDB/sawonDB.csv', names = ['sabun', 'saname', 'deptno', 'sajob', 'sapay', 'sahire', 'sasex', 'samgr'], header = None)
gogekDB = pandas.read_csv('./data/data/sawonDB/gogekDB.csv', names = ['gobun', 'goname', 'gotel', 'gojumin', 'godam'], header = None)


# In[13]:


# ' 전처리 후 저장
deptDB = deptDB.replace('\'','',regex=True)
sawonDB = sawonDB.replace('\'','',regex=True)
gogekDB = gogekDB.replace('\'','',regex=True)


# In[14]:


# 공백 전처리 후 저장
deptDB_str = deptDB[:]
deptDB_str['dname'] = deptDB_str['dname'].str.strip()
deptDB_str['loc'] = deptDB_str['loc'].str.strip()

sawonDB_str = sawonDB[:]
sawonDB_str['saname'] = sawonDB_str['saname'].str.strip()
sawonDB_str['sajob'] = sawonDB_str['sajob'].str.strip()
sawonDB_str['sahire'] = sawonDB_str['sahire'].str.strip()
sawonDB_str['sasex'] = sawonDB_str['sasex'].str.strip()

gogekDB_str = gogekDB[:]
gogekDB_str['goname'] = gogekDB_str['goname'].str.strip()
gogekDB_str['gotel'] = gogekDB_str['gotel'].str.strip()
gogekDB_str['gojumin'] = gogekDB_str['gojumin'].str.strip()


# In[9]:


desa = sawonDB_str.merge(deptDB_str, how = 'inner', on = 'deptno')
desa = desa.sort_values('sabun')
desa.head(10)


# In[15]:


quest = desa[desa['dname'] == '전산부']
print('전산부 직원의 평균 연봉 : ', quest['sapay'].mean())

