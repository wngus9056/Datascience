
# coding: utf-8

# Pandas04_06_readExcel02_김주현

# In[1]:


import pandas


# In[22]:


df1 = pandas.read_excel('./DataSet/datalabPractice01.xlsx')
df2 = pandas.read_excel('./DataSet/datalabPractice01.xlsx', sheet_name = 'Sheet1', usecols = [1, 2], skiprows = [2], skipfooter = 4, header = None)


# In[23]:


print(df1)


# In[24]:


print(df2.columns, '\n')
print(df2, '\n')

