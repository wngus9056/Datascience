
# coding: utf-8

# Pandas02_04_FunEx9_김주현

# In[1]:


#함수 안에서 함수 밖의 변수를 변경하는 방법

#1. return 사용하기


# In[2]:


a = 1
def vartest(a):
    a = a+1
    return a

a = vartest(a)
print(a)
print('-'*15)


# In[4]:


b = 1
def vartest():
    global b
    b = b + 1
    
vartest()
print(b)
print('-'*15)

