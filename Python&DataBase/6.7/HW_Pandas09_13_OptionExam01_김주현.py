
# coding: utf-8

# HW_Pandas09_13_OptionExam01_김주현

# In[2]:


import pandas


# In[3]:


deptDB = pandas.read_csv('./data/data/sawonDB/deptDB.csv',names = ['deptno', 'dname', 'loc'], header = None)
sawonDB = pandas.read_csv('./data/data/sawonDB/sawonDB.csv', names = ['sabun', 'saname', 'deptno', 'sajob', 'sapay', 'sahire', 'sasex', 'samgr'], header = None)
gogekDB = pandas.read_csv('./data/data/sawonDB/gogekDB.csv', names = ['gobun', 'goname', 'gotel', 'gojumin', 'godam'], header = None)


# In[4]:


# ' 전처리 후 저장
deptDB = deptDB.replace('\'','',regex=True)
sawonDB = sawonDB.replace('\'','',regex=True)
gogekDB = gogekDB.replace('\'','',regex=True)


# In[5]:


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


# In[11]:


nlist = []
name_input = input('월급을 확인하고자하는 사원의 이름을 입력하세요 : ')
for index, idx in enumerate(sawonDB_str['saname']):
    if idx == name_input:
        nlist.append(index)
print(sawonDB_str.iloc[nlist]['sapay'])


# In[10]:


nlist = []
name_input = input('월급을 확인하고자하는 사원의 이름을 입력하세요 : ')
for index, idx in enumerate(sawonDB_str['saname']):
    if idx == name_input:
        nlist.append(index)
if int(sawonDB_str.iloc[nlist]['sapay']) >= 3000:
    print('상위소득자')
elif int(sawonDB_str.iloc[nlist]['sapay']) >= 2000:
    print('중간소득자')
else:
    print('월급 조정 대상자')

