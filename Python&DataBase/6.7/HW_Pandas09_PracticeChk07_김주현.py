
# coding: utf-8

# HW_Pandas09_PracticeChk07_김주현

# In[1]:


import pandas


# In[2]:


Animal = ['오렌지', '장미', '바다', '여우']


# In[3]:


for a in Animal:
    print(a)


# In[4]:


# 인덱스와 함께 값 출력
for b, c in enumerate(Animal):
    print(b, c)


# In[5]:


# 옵션으로 넣어준 숫자부터 인덱스 출력
for b, c in enumerate(Animal, 2):
    print(b, c)

