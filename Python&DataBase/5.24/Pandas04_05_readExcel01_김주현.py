
# coding: utf-8

# Pandas04_05_readExcel01_김주현

# In[1]:


import pandas as pd


# In[2]:


file_pathExcel = './DataSet/datalabPractice01.xlsx'
dfExcel = pd.read_excel(file_pathExcel)


# In[3]:


print(dfExcel)

