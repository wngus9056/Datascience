
# coding: utf-8

# In[2]:


import pandas
import seaborn


# In[3]:


titanic = seaborn.load_dataset('titanic')


# In[5]:


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

total = pandas.concat([age10_df, age20_df, age30_df,                        age40_df, age50_df, age60_df, age70_df, age80_df, age90_df])

total_uni = total['연령'].unique()

total.groupby(['연령', 'sex'])['survived'].count()

