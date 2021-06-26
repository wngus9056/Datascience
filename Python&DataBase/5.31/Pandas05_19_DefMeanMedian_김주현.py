
# coding: utf-8

# Pandas05_19_DefMeanMedian_김주현

# In[242]:


num = [28, 31, 24, 25, 30, 32, 20, 30, 31, 26, 31]
test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c=[]


# In[160]:


# def mMean():
#     print((sum(num)/len(num)))
    
# def mMedian():
#     a = len(num)/2
#     num.sort()
#     if len(num) % 2 == 1:
#         print(num[round(a)-1])
#     else:
#         print((num[round(a)+1]+num[round(a)]+2)/2)
        


# In[243]:


def mMean1():
    print((sum(test)/len(test)))
    
def mMedian1():
    a = len(test)/2
    test.sort()
    if len(test) % 2 == 1:
        print(test[round(a)-1])
    else:
        print((test[round(a)]+test[round(a)]-1)/2)
        
# def mDeviation():
#     m = sum(test)/len(test)
#     for a in range(len(test)):
#         dev = test[a] - m
#         c.append(dev)
#     print(c)


# In[244]:


mMean1()


# In[245]:


mMedian1()


# In[246]:


# mDeviation()

