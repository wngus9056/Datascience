
# coding: utf-8

# HW_Pandas09_PracticeChk03_김주현

# In[2]:


import pandas


# In[3]:


deptDB = pandas.read_csv('./data/data/sawonDB/deptDB.csv',names = ['deptno', 'dname', 'loc'], header = None)
sawonDB = pandas.read_csv('./data/data/sawonDB/sawonDB.csv', names = ['sabun', 'saname', 'deptno', 'sajob', 'sapay', 'sahire', 'sasex', 'samgr'], header = None)
gogekDB = pandas.read_csv('./data/data/sawonDB/gogekDB.csv', names = ['gobun', 'goname', 'gotel', 'gojumin', 'godam'], header = None)


# In[4]:


deptDB = deptDB.replace('\'','',regex=True)
sawonDB = sawonDB.replace('\'','',regex=True)
gogekDB = gogekDB.replace('\'','',regex=True)


# In[ ]:


print(deptDB)
print('-'*30)
print(sawonDB)
print('-'*30)
print(gogekDB)


# In[6]:


# SawonDB 데이터에서 입사년도가 88년도인 사원 출력.
q1 = sawonDB[:]
for a in range(len(q1)):
    if q1['sahire'][a][3:5] == str(88):
        print(q1['sabun'][a], q1['saname'][a])


# In[5]:


# Strip으로 전처리 후 SawonDB 데이터에서 입사년도가 88년도인 사원 출력.
# Fix.ver
q1 = sawonDB[:]
for a in range(len(q1)):
    if q1['sahire'].str.strip()[a][2:4] == str(88):
        print(q1['sabun'][a], q1['saname'][a])

