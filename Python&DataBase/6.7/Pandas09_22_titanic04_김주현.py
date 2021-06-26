
# coding: utf-8

# In[1]:


import pandas
import seaborn


# In[2]:


titanic = seaborn.load_dataset('titanic')


# In[3]:


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
    if (titanic['age'][a] < 20) and (titanic['survived'][a] == 0):
        age10.append(titanic.iloc[a])
    elif titanic['age'][a] < 30 and (titanic['survived'][a] == 0):
        age20.append(titanic.iloc[a])
    elif titanic['age'][a] < 40 and (titanic['survived'][a] == 0):
        age30.append(titanic.iloc[a])
    elif titanic['age'][a] < 50 and (titanic['survived'][a] == 0):
        age40.append(titanic.iloc[a])
    elif titanic['age'][a] < 60 and (titanic['survived'][a] == 0):
        age50.append(titanic.iloc[a])
    elif titanic['age'][a] < 70 and (titanic['survived'][a] == 0):
        age60.append(titanic.iloc[a])
    elif titanic['age'][a] < 80 and (titanic['survived'][a] == 0):
        age70.append(titanic.iloc[a])
    elif titanic['age'][a] < 90 and (titanic['survived'][a] == 0):
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

total = pandas.concat([age10_df, age20_df, age30_df,                        age40_df, age50_df, age60_df, age70_df, age80_df, age90_df])

total_uni = total['연령'].unique()

total.groupby(['연령', 'sex'])['survived'].count()


# In[6]:


# 연령대별 사망자수 남녀 사망자수
age0 = []
age10 = []
age20 = []
age30 = []
age40 = []
age50 = []
age60 = []
age70 = []
age80 = []
for a in range(len(titanic)):
    if (titanic['age'][a] < 10) and (titanic['survived'][a] == 0):
        age0.append(titanic.iloc[a])
    elif (titanic['age'][a] < 20) and (titanic['survived'][a] == 0):
        age10.append(titanic.iloc[a])
    elif titanic['age'][a] < 30 and (titanic['survived'][a] == 0):
        age20.append(titanic.iloc[a])
    elif titanic['age'][a] < 40 and (titanic['survived'][a] == 0):
        age30.append(titanic.iloc[a])
    elif titanic['age'][a] < 50 and (titanic['survived'][a] == 0):
        age40.append(titanic.iloc[a])
    elif titanic['age'][a] < 60 and (titanic['survived'][a] == 0):
        age50.append(titanic.iloc[a])
    elif titanic['age'][a] < 70 and (titanic['survived'][a] == 0):
        age60.append(titanic.iloc[a])
    elif titanic['age'][a] < 80 and (titanic['survived'][a] == 0):
        age70.append(titanic.iloc[a])
    elif titanic['age'][a] < 90 and (titanic['survived'][a] == 0):
        age80.append(titanic.iloc[a])

age0_df = pandas.DataFrame(age0)
age0_df['연령'] = '0대'        
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

total = pandas.concat([age0_df, age10_df, age20_df, age30_df,                        age40_df, age50_df, age60_df, age70_df, age80_df])

total_uni = total['연령'].unique()

total.groupby(['연령', 'sex'])['survived'].count()


# In[ ]:


# 또 다른
ages = list(range(0, 90, 10))

for a in ages:
    start = a
    end = a+10
    ageTemp = titanic[(titanic['age'] >= start) & (titanic['age'] < end) & (titanic['survived'] == 0)]
    print('{}세 이상 - {}세 미만 사망자수 : {}'          .format(start, end, ageTemp['survived'].count()))


# In[ ]:


# Plus 남녀 나눠서
ages = list(range(0, 90, 10))

for a in ages:
    start = a
    end = a+10
    ageTemp = titanic[(titanic['age'] >= start) & (titanic['age'] < end) & (titanic['survived'] == 0)]
    print('{}세 이상 - {}세 미만 사망자수'.format(start, end))
    print(ageTemp.groupby('sex')['survived'].count())
    print('-'*60)


# In[ ]:


age70_df[age70_df['survived'] == 0]


# In[ ]:


age60_df[:]


# In[ ]:


titanic[(titanic['age'] >= 60) & (titanic['age'] < 70)]


# In[ ]:


titanic


# In[ ]:


for x in ages:
    start = x
    end = x+10
    ageTemp = titanic[(titanic['age'] >= start) & (titanic['age'] < end)]
    print(ageTemp['sex'][ageTemp['survived'] == 0].count(),ageTemp['sex'][ageTemp['survived'] == 1].count())

