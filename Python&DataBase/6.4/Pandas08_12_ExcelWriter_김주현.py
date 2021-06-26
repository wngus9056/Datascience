
# coding: utf-8

# Pandas08_12_ExcelWriter_김주현

# In[1]:


import pandas


# In[4]:


#json
data = {'name' : ['Jerry', 'Rial', 'Paul'],       'algol' : ['A', 'A+', 'B'],       'basic' : ['C', 'B', 'B+'],       'c++' : ['B+', 'C', 'C+']}

df = pandas.DataFrame(data)
df.set_index('name', inplace = True)

df.to_json('./../df_sample.json')


# In[5]:


#excel
data = {'name' : ['Jerry', 'Rial', 'Paul'],       'algol' : ['A', 'A+', 'B'],       'basic' : ['C', 'B', 'B+'],       'c++' : ['B+', 'C', 'C+']}

df = pandas.DataFrame(data)
df.set_index('name', inplace = True)

df.to_excel('./../df_sample.xlsx')


# In[8]:


#excelwriter
data1 = {'name' : ['Jerry', 'Rial', 'Paul'],       'algol' : ['A', 'A+', 'B'],       'basic' : ['C', 'B', 'B+'],       'c++' : ['B+', 'C', 'C+']}
data2 = {'c0' : [1, 2, 3],        'c1' : [4, 5, 6],        'c2' : [7, 8, 9],        'c3' : [10, 11, 12],        'c4' : [13, 14, 15]}

df1 = pandas.DataFrame(data1)
df1.set_index('name', inplace = True)

df2 = pandas.DataFrame(data2)
df2.set_index('c0', inplace = True)

writer = pandas.ExcelWriter('./../df_excelwriter.xlsx')
df1.to_excel(writer, sheet_name = '시트1')
df2.to_excel(writer, sheet_name = '시트2')
writer.save()
# df1.to_excel(pandas.ExcelWriter('./../df_excelwriter.xlsx'), sheet_name = '시트1')
# df2.to_excel(pandas.ExcelWriter('./../df_excelwriter.xlsx'), sheet_name = '시트2')
# pandas.ExcelWriter('./../df_excelwriter.xlsx').save()

