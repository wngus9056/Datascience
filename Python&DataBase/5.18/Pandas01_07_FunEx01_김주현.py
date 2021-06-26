
# coding: utf-8

# Pandas01_07_FunEx01_김주현

# ## 기본 함수 선언 연습
# <h1>기본 연습</h1>
# <h2>기본 연습</h2>
# 
# HTML : Hyper Text Markup Language

# In[5]:


def add(a,b):
    return a+b

a = 3
b = 4
c = add(a,b)

print('%d + %d = %d' %(a, b, c))


# 1. 일반적인 함수

# In[6]:


def add(a,b):
    return a, b, a+b

a, b, result = add(b=5, a=3)
print('%d + %d = %d' %(b, a, result))


# 2. 입력 값이 없는 함수

# In[7]:


def say():
    return('Hi')
print(say())


# 3. 결괏값이 없는 함수

# In[8]:


#결괏값은 오직 return명령어로만 돌려받을 수 있다.
def add2(a, b):
    print('%d, %d의 합은 %d입니다.' %(a, b, a+b))

print(add2(3,4))


# 4. 입력값도 결괏값도 없는 함수

# In[9]:


def say2():
    print('Hi')
    
print(say2())

