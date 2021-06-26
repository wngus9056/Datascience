
# coding: utf-8

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


# In[ ]:


sawonDB_str.head(10)


# In[ ]:


# 문제 12] 부서번호가 10번, 20번인 사원들의 이름과 월급과 부서번호를 출력하시오.

for a in range(len(sawonDB_str)):
    if sawonDB_str['deptno'][a] == 10 or sawonDB_str['deptno'][a] == 20 :
        print('부서번호가 ',sawonDB_str['deptno'][a],'인',               sawonDB_str['saname'][a], '의 월급은',               sawonDB_str['sapay'][a], '입니다.')


# In[27]:


job_chk = sawonDB_str[sawonDB_str['deptno'].isin(['10', '20'])]
jlist = []
for index, idx in enumerate(sawonDB_str['deptno']):
    if idx == 10 or idx == 20:
        jlist.append(index)
        
print(sawonDB_str.iloc[jlist][['saname', 'sapay', 'deptno']])


# In[5]:


# 문제 13] 급여가 1000 ~ 3000 사이의 직원 이름과 급여 출력하시오.

for a in range(len(sawonDB_str)):
    if sawonDB_str['sapay'][a] >= 1000 and sawonDB_str['sapay'][a] <= 3000:
        print('급여가 1000 ~ 3000 사이인 직원의 이름과 급여는',              sawonDB_str['saname'][a], sawonDB_str['sapay'][a], '입니다.')


# In[ ]:


# 문제 21] 직업을 물어보게 하고 직업을 입력하면 
# 해당 직업인 사원들의 이름과 직업이 출력되게 하는데 
# 없는 직업을 입력하면 해당 직업은 없습니다. 라는 메세지가 출력되게 하시오.

while True:
    print()
    job = input('확인하고자 하는 직업을 입력해주세요 : \t\t없음 = 종료')
    if job == '없음':
        print('종료합니다.')
        break
    elif job == '회장':
        print()
        for a in range(len(sawonDB_str)):
            if sawonDB_str['sajob'][a] == '회장':
                print(sawonDB_str['sajob'][a], sawonDB_str['saname'][a])
    elif job == '부장':
        print()
        for a in range(len(sawonDB_str)):
            if sawonDB_str['sajob'][a] == '부장':
                print(sawonDB_str['sajob'][a], sawonDB_str['saname'][a])
    elif job == '과장':
        print()
        for a in range(len(sawonDB_str)):
            if sawonDB_str['sajob'][a] == '과장':
                print(sawonDB_str['sajob'][a], sawonDB_str['saname'][a])
    elif job == '사원':
        print()
        for a in range(len(sawonDB_str)):
            if sawonDB_str['sajob'][a] == '사원':
                print(sawonDB_str['sajob'][a], sawonDB_str['saname'][a])
    elif job == '대리':
        print()
        for a in range(len(sawonDB_str)):
            if sawonDB_str['sajob'][a] == '대리':
                print(sawonDB_str['sajob'][a], sawonDB_str['saname'][a])
    else:
        print()
        print('해당 직업은 없습니다.')
        continue
    


# In[9]:


name = input()
b = sawonDB[sawonDB['sajob'].isin([name])]
c = sawonDB['sajob'].unique()

if a in c:
    print(b[['sajob','saname']])
else:
    print('해당 직업은 없습니다.')


# In[25]:


aaa = sawonDB_str[sawonDB_str['sajob'].isin(['대리','과장'])]
print(aaa)

