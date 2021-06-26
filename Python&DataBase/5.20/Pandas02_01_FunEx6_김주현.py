
# coding: utf-8

# Pandas02_01_FunEx6_김주현

# In[1]:


#return 문을 2번 사용하면
#두 번째 return 문인 return a*b는 실행되지 않는다.


# In[2]:


def add_and_mul(a,b):
    return a+b
    return a*b

result = add_and_mul(3,4)
print(result)
print('-'*15)


# In[3]:


#[return의 또 다른 쓰임새]
#return을 단독으로 써서 함수를 즉시 빠져나갈 수 있다.


# In[5]:


def say_nick(nick):
    if nick == '바보':
        return
    print('나의 별명은 %s입니다.'%nick)

say_nick('야호')
say_nick('바보')
print('-'*15)

