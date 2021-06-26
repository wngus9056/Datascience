
# coding: utf-8

# HW_Pandas09_PracticeChk06_김주현

# In[1]:


import pandas


# In[2]:


test = pandas.Series(['Mouse', 'dog', 'house and parrot', '23'])


# In[11]:


# 대소문자를 가린 'og'를 포함한 것을 True, False로 출력
test.str.contains('og')


# In[12]:


# 대소문자를 가리지 않은 'oG'를 포함한 것을 True, False로 출력
test.str.contains('oG', case = False)


# In[14]:


# 'house'와 'dog'를 포함한 것을 True, False로 출력  
#  | 는 or의 의미
test.str.contains('house|dog')


# In[13]:


# 숫자를 포함한 것을 True, False로 출력
test.str.contains('\\d')

