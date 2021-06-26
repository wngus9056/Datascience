
# coding: utf-8

# Pandas08_02_SeriesOper02nan_김주현

# In[1]:


import pandas
import numpy


# In[5]:


student1 = pandas.Series({'국어' : numpy.nan, '영어' : 80, '수학' : 90})
student2 = pandas.Series({'수학' : 80, '국어' : 80})


# In[8]:


print(student1)
print('-'*20)
print(student2)


# In[9]:


add = student1 + student2
subtraction = student1 - student2
multiplication = student1 * student2
div = student1 / student2


# In[11]:


a = pandas.DataFrame([add, subtraction, multiplication, div], index = ['덧셈', '뺄셈', '곱셈', '나눗셈'])


# In[12]:


print(a)


# In[21]:


re_add = student1.add(student2, fill_value = 0)
re_subtraction = student1.sub(student2, fill_value = 0)
re_multiplication = student1.mul(student2, fill_value = 0)
re_div = student1.div(student2, fill_value = 0)


# In[22]:


re_a = pandas.DataFrame([re_add, re_subtraction, re_multiplication, re_div],                         index = ['덧셈', '뺄셈', '곱셈', '나눗셈'])


# In[23]:


print(re_add)
print('-'*20)
print(re_subtraction)
print('-'*20)
print(re_multiplication)
print('-'*20)
print(re_div)


# In[24]:


print(re_a)

