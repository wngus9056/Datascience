
# coding: utf-8

# HW_Pandas09_PracticeChk04_김주현

# In[2]:


import pandas


# In[15]:


deptDB = pandas.read_csv('./data/data/sawonDB/deptDB.csv',names = ['deptno', 'dname', 'loc'], header = None)
sawonDB = pandas.read_csv('./data/data/sawonDB/sawonDB.csv', names = ['sabun', 'saname', 'deptno', 'sajob', 'sapay', 'sahire', 'sasex', 'samgr'], header = None)
gogekDB = pandas.read_csv('./data/data/sawonDB/gogekDB.csv', names = ['gobun', 'goname', 'gotel', 'gojumin', 'godam'], header = None)


# In[16]:


deptDB = deptDB.replace('\'','',regex=True)
sawonDB = sawonDB.replace('\'','',regex=True)
gogekDB = gogekDB.replace('\'','',regex=True)


# In[ ]:


print(deptDB)
print('-'*30)
print(sawonDB)
print('-'*30)
print(gogekDB)


# In[43]:


q2.head()


# In[6]:


# Q 01] SawonDB 데이터에서 입사년도가 88년도인 사원 출력.
q1 = sawonDB[:]
for a in range(len(q1)):
    if q1['sahire'][a][3:5] == str(88):
        print(q1['sabun'][a], q1['saname'][a])


# In[5]:


# Q 01] Fix.ver
# Strip으로 전처리 후 SawonDB 데이터에서 입사년도가 88년도인 사원 출력.
q1 = sawonDB[:]
for a in range(len(q1)):
    if q1['sahire'].str.strip()[a][2:4] == str(88):
        print(q1['sabun'][a], q1['saname'][a])


# In[40]:


deptDB.head()


# In[46]:


# 데이터베이스들의 공백 전처리
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


# In[47]:


# 공백 전처리 반증
test_sawon = sawonDB_str[:]
for a in range(len(test_sawon)):
    if test_sawon['sahire'][a][2:4] == str(88):
        print(test_sawon['sabun'][a], test_sawon['saname'][a])


# In[ ]:


# deptDB_str = deptDB.replace(' ', '', regex = True)
# sawonDB_str = sawonDB.replace(' ', '', regex= True)
# gogekDB_str = gogekDB.replace(' ', '', regex = True)

