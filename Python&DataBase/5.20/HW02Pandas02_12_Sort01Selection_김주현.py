
# coding: utf-8

# HW02Pandas02_12_Sort01Selection_김주현

# In[16]:


random01 = [2, 5, 4, 8, 84, 67, 24, 91, 18, 33, 57, 11, 55, 46, 82, 154, 5]


# In[17]:


for x in range(len(random01)-1):
	for y in range(x+1, len(random01)):
		if random01[x] > random01[y]:
			temp = random01[x]
			random01[x] = random01[y]
			random01[y] = temp
			print(temp, end=' ')
		else:
			continue
print(random01)

