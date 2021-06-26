
# coding: utf-8

# Pandas07_05_SeriesChk02Doit_김주현

# In[1]:


import pandas


# In[3]:


sc = pandas.DataFrame({'Name' : ['Rosaline Franklin', 'William Gosset'],                       'Occupation' : ['Chemist', 'Statistician'],                      'Born' : ['1920-07-25', '1876-06-13'],                      'Died' : ['1958-04-16', '1937-10-16'],                      'Age' : [37, 61]})
print(sc)


# In[4]:


sc1 = pandas.DataFrame({'Name' : ['Rosaline Franklin', 'William Gosset'],                       'Occupation' : ['Chemist', 'Statistician'],                      'Born' : ['1920-07-25', '1876-06-13'],                      'Died' : ['1958-04-16', '1937-10-16'],                      'Age' : [37, 61]},
                      index = ['Rosaline Franklin', 'William Gosset'],
                      columns = ['Occupation', 'Born', 'Age', 'Died'])
print(sc1)


# In[6]:


from collections import OrderedDict

sc2 = pandas.DataFrame([('Name', ['Rosaline Franklin', 'William Gosset']),
                       ('Ocuupation', ['Chemist', 'Statistician']),
                       ('Born', ['1920-07-25', '1876-06-13']),
                       ('Died', ['1958-04-16', '1937-10-16']),
                       ('Age', [37, 61])])
print(sc2)
print(type(sc2[0]))


# In[7]:


sc3 = pandas.DataFrame(OrderedDict([('Name', ['Rosaline Franklin', 'William Gosset']),
                       ('Ocuupation', ['Chemist', 'Statistician']),
                       ('Born', ['1920-07-25', '1876-06-13']),
                       ('Died', ['1958-04-16', '1937-10-16']),
                       ('Age', [37, 61])]))
print(sc3)

