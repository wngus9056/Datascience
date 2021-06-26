
# coding: utf-8

# Pandas01_11_FunEx05_김주현

# In[1]:


'''
함수의 결괏값은 언제나 하나이다.
튜플값 하나인 (a+b, a*b)로 돌려준다.
'''
def add_and_mul(a,b):
    return a+b, a*b

result = add_and_mul(3,4)
print(result)

# 튜플 값을 2개의 결괏값으로 받고 싶으면
result1, result2 = add_and_mul(3,4)
print(result1, result2)

