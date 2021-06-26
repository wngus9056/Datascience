
# coding: utf-8

# Pandas01_09_FunEx03_김주현

# In[1]:


def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result = result + i
    elif choice == 'mul':
        result = 1
        for i in args:
            result = result * i
    return result

result1 = add_mul('add',2,3)
print(result1)
print('-'*15)

result2 = add_mul('mul',2,3)
print(result2)

