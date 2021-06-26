
# coding: utf-8

# Pandas08_01_SeriesOper01_김주현

# In[1]:


import pandas


# In[2]:


student1 = pandas.Series({'국어' : 100, '영어' : 80, '수학' : 90})
student2 = pandas.Series({'영어' : 80, '수학' : 80, '국어' : 80})


# In[3]:


percentage = student1 / 200
print(percentage)
print('-'*20)
print(type(percentage))


# In[9]:


add = student1 + student2
subtraction = student1 - student2
multiplication = student1 * student2
div = student1 / student2


# In[11]:


e = pandas.DataFrame([add, subtraction, multiplication, div], index = ['덧셈', '뺄셈', '곱셈', '나눗셈'])


# In[15]:


print(type(div))
print('-'*20)
print(e, '\n', type(e))


# In[19]:


print(add, '\n', subtraction, '\n', multiplication, '\n', div, '\n')

