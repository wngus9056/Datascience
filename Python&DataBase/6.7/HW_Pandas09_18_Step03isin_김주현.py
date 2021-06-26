
# coding: utf-8

# In[22]:


import pandas


# In[23]:


deptDB = pandas.read_csv('./data/data/sawonDB/deptDB.csv',names = ['deptno', 'dname', 'loc'], header = None)
sawonDB = pandas.read_csv('./data/data/sawonDB/sawonDB.csv', names = ['sabun', 'saname', 'deptno', 'sajob', 'sapay', 'sahire', 'sasex', 'samgr'], header = None)
gogekDB = pandas.read_csv('./data/data/sawonDB/gogekDB.csv', names = ['gobun', 'goname', 'gotel', 'gojumin', 'godam'], header = None)


# In[24]:


# ' 전처리 후 저장
deptDB = deptDB.replace('\'','',regex=True)
sawonDB = sawonDB.replace('\'','',regex=True)
gogekDB = gogekDB.replace('\'','',regex=True)


# In[25]:


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


# In[37]:


job_chk = sawonDB_str[sawonDB_str['sajob'].isin(['과장', '사원'])]


# In[38]:


job_chk


# In[39]:


job_cntchk = job_chk.groupby(['sajob'])['sabun'].count() >= 4


# In[40]:


job_final = job_cntchk[job_cntchk.values]


# In[41]:


for index, idx in enumerate(job_final.index):
    cal = sawonDB_str[sawonDB_str['sajob'] == idx]
    print(cal.groupby('sajob')['sapay'].mean())

