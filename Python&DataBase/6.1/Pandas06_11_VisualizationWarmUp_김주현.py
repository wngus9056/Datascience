
# coding: utf-8

# Pandas06_11_VisualizationWarmUp_김주현

# In[11]:


import pandas
import matplotlib


# In[12]:


df = pandas.read_csv('./data/data/gapminder.tsv',sep='\t')


# In[13]:


vis = df.groupby('year')['lifeExp'].mean()


# In[16]:


print(vis.plot())


# In[17]:


get_ipython().run_line_magic('matplotlib', 'inline')
print(vis.plot())

