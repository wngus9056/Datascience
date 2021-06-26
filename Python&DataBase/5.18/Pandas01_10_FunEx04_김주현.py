
# coding: utf-8

# Pandas01_10_FunEx04_김주현

# In[3]:


def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', age=3)

