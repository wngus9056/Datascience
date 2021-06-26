
# coding: utf-8

# Pandas02_10_FileIOEx04_김주현

# In[1]:


#3. read 함수 사용하기


# In[2]:


f = open('새파일.txt', 'r')
data = f.read()
print(data)
f.close()

