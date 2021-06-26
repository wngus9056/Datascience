
# coding: utf-8

# Pandas07_17_titanicAnlaysis02_김주현

# In[1]:


import pandas
import seaborn


# In[2]:


titanic = seaborn.load_dataset('titanic')


# In[3]:


titanic.head(3)


# In[4]:


# 행렬 Chk
print(titanic.shape)


# In[5]:


# 컬럼명 Chk
print(titanic.columns)


# In[6]:


# 컬럼 유니크 값
for a in titanic.columns:
    print(a,'의 유니크 값 : ',titanic[a].unique())
    print('-'*90)


# In[7]:


# 나이 최소,최대
print('최소 나이는',titanic['age'].min(),'이고,', '최대 나이는',titanic['age'].max(),'입니다.')


# In[8]:


# 성별 survived 개수
print(titanic.groupby(['sex', 'survived'])['survived'].count())


# In[9]:


# 남자, 여자 명수
print(titanic.groupby('sex')['survived'].count())


# In[10]:


# 연령대별 사망자수 남녀 사망자수
age10 = []
age20 = []
age30 = []
age40 = []
age50 = []
age60 = []
age70 = []
age80 = []
age90 = []
for a in range(len(titanic)):
    if titanic['age'][a] < 20:
        age10.append(titanic.iloc[a])
    elif titanic['age'][a] < 30:
        age20.append(titanic.iloc[a])
    elif titanic['age'][a] < 40:
        age30.append(titanic.iloc[a])
    elif titanic['age'][a] < 50:
        age40.append(titanic.iloc[a])
    elif titanic['age'][a] < 60:
        age50.append(titanic.iloc[a])
    elif titanic['age'][a] < 70:
        age60.append(titanic.iloc[a])
    elif titanic['age'][a] < 80:
        age70.append(titanic.iloc[a])
    elif titanic['age'][a] < 90:
        age80.append(titanic.iloc[a])
    else:
        age90.append(titanic.iloc[a])
        
age10_df = pandas.DataFrame(age10)
age10_df['연령'] = '10대'
age20_df = pandas.DataFrame(age20)
age20_df['연령'] = '20대'
age30_df = pandas.DataFrame(age30)
age30_df['연령'] = '30대'
age40_df = pandas.DataFrame(age40)
age40_df['연령'] = '40대'
age50_df = pandas.DataFrame(age50)
age50_df['연령'] = '50대'
age60_df = pandas.DataFrame(age60)
age60_df['연령'] = '60대'
age70_df = pandas.DataFrame(age70)
age70_df['연령'] = '70대'
age80_df = pandas.DataFrame(age80)
age80_df['연령'] = '80대'
age90_df = pandas.DataFrame(age90)
age90_df['연령'] = '90대'

total = pandas.concat([age10_df, age20_df, age30_df, age40_df,                       age50_df, age60_df, age70_df, age80_df, age90_df])

total_uni = total['연령'].unique()

total.groupby(['연령', 'sex'])['survived'].count()

