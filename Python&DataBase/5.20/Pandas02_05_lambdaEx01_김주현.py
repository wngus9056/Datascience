
# coding: utf-8

# Pandas02_05_lambdaEx01_김주현

# In[2]:


#lanbda
'''
lambda는 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 한다.
보통 함수를 한줄로 간결하게 만들 때 사용한다.
우리말로는 '람다'라고 읽고 def를 사용해야 할 정도로 복잡하지 않거나
def를 사용할 수 없는 곳에 주로 쓰인다.
'''


# In[3]:


#사용형식
# lambda 매개변수1, 매개변수~, ...: 매개변수를 이용한 표현식


# In[5]:


add = lambda a,b:a+b
result = add(3,6)
print(result)


# In[6]:


def add(a,b):
    return a+b
result = add(3,5)
print(result)

