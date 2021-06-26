
# coding: utf-8

# Pandas07_00_SawonDBPractice02_김주현

# In[1]:


import pandas


# In[76]:


deptDB = pandas.read_csv('./data/data/sawonDB/deptDB.csv',names = ['deptno', 'dname', 'loc'], header = None)
sawonDB = pandas.read_csv('./data/data/sawonDB/sawonDB.csv', names = ['sabun', 'saname', 'deptno', 'sajob', 'sapay', 'sahire', 'sasex', 'samgr'], header = None)
gogekDB = pandas.read_csv('./data/data/sawonDB/gogekDB.csv', names = ['gobun', 'goname', 'gotel', 'gojumin', 'godam'], header = None)


# In[77]:


deptDB = deptDB.replace('\'','',regex=True)
sawonDB = sawonDB.replace('\'','',regex=True)
gogekDB = gogekDB.replace('\'','',regex=True)


# In[78]:


print(deptDB)
print('-'*30)
print(sawonDB)
print('-'*30)
print(gogekDB)


# In[79]:


sawonDB.head(3)


# In[80]:


#SawonDB 데이터에서 입사년도가 88년도인 사원 출력.

q1 = sawonDB[:]
for a in range(len(q1)):
    if q1['sahire'][a][3:5] == str(88):
        print(q1['sabun'][a], q1['saname'][a])


# In[83]:


#SawonDB 데이터에서 4월에 입사한 사원을 출력.

q2 = sawonDB[:]
for a in range(len(q2)):
    if q2['sahire'][a][7] == str(4):
        print(q2['sabun'][a],q2['saname'][a])


# In[82]:


#SawonDB 데이터에서 사원번호가 짝수인 사람만 출력.

q3 = sawonDB.sort_values('sabun')
for a in range(len(q3)):
    if q3['sabun'][a] % 2 == 0:
        print(q3['sabun'][a], q3['saname'][a])


# In[84]:


#SawonDB 데이터에서 직위별 급여 평균을 출력.

q4 = sawonDB.groupby('sajob')['sapay'].mean()
print(q4)


# In[85]:


#SawonDB 데이터에서 직위별, 성별 평균을 출력.

q5 = sawonDB.groupby(['sajob', 'sasex'])['sapay'].mean()
print(q5)


# In[86]:


#SawonDB 데이터에서 급여 10% 인상 후 인상급여 필드 추가 확인

for a in range(len(sawonDB)):
    print(sawonDB['sabun'][a], sawonDB['saname'][a], sawonDB['sapay'][a]*1.1)


# In[87]:


# sawonDB 데이터에서 전산부 직원의 평균연봉 출력.

test = sawonDB[:]
test.loc[(test.deptno == 10), 'deptno'] = '총무부'
test.loc[(test.deptno == 20), 'deptno'] = '영업부'
test.loc[(test.deptno == 30), 'deptno'] = '전산부'
test.loc[(test.deptno == 40), 'deptno'] = '관리부'

test1 = test.groupby('deptno')['sapay'].mean()
print('전산부 직원의 평균연봉은',test1['전산부'],'원 입니다.')


# In[88]:


test2 = sawonDB[:]
change_values = {10 : '총무부', 20 : '영업부', 30 : '전산부', 40 : '관리부'}
test2 = test2.replace({'deptno' : change_values})

test2 = test2.groupby('deptno')['sapay'].mean()
print('전산부 직원의 평균연봉은',test2['전산부'],'원 입니다.')


# In[89]:


# 컬럼 이름순 재배치, sort_values() 함수 적용

q8 = sawonDB.sort_values('saname')
print(q8)


# In[90]:


# sawonDB 데이터에서 직위가 사원과 대리 중 직원수가 4인이상인 직위, 평균급여 출력
q9 = sawonDB['sajob'].unique()
schk = []
dchk = []
gr_job = sawonDB.groupby('sajob')

for a in range(len(sawonDB)):
    if sawonDB['sajob'][a] == ' 사원':
        schk.append(sawonDB['sajob'][a])
    elif sawonDB['sajob'][a] == ' 대리':
        dchk.append(sawonDB['sajob'][a])
        
sum_s = (gr_job['sapay'].sum())/len(schk)
sum_d = (gr_job['sapay'].sum())/len(dchk)

if len(schk) >= 4:
    print('직원수가 4인 이상인 직위는 {}이고, 평균급여는 {}원 입니다.'.format(schk[0], sum_s[3]))
if len(dchk) >= 4:
    print('직원수가 4인 이상인 직위는 {}이고, 평균급여는 {}원 입니다.'.format(dchk[0], sum_s[1]))

