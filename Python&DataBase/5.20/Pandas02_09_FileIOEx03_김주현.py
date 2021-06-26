
# coding: utf-8

# Pandas02_09_FileIOEx03_김주현

# In[1]:


#2. readlines() 함수 사용하기


# In[2]:


f = open('새파일.txt', 'r')
lines = f.readlines()
print(lines)

for line in lines:
    print(line)
f.close()

