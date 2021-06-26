
# coding: utf-8

# Pandas02_02_FunEx7_김주현

# In[1]:


#매개변수에 초깃값 미리 설정하기
#say_myself 함수는 3개의 매개변수를 받아서 마지막 인수인
#man이 True이면 '남자입니다.', False이면 '여자입니다.'를 출력


# In[4]:


def say_myself(name, old, man=True):
    print('나의 이름은 %s입니다.'%name)
    print('나이는 %d입니다.'%old)
    if man:
        print('남자입니다.')
    else:
        print('여자입니다.')

say_myself('김주현',27)
print('-'*15)
say_myself('김주현',27,False)
print('-'*15)

