
# coding: utf-8

# Pandas06_01_DefStandardDeviation_김주현

# In[506]:


num = [28, 31, 24, 25, 30, 32, 20, 30, 31, 26, 31]


# In[507]:


def mMean():
    print((sum(num)/len(num)))
    
def mMedian():
    a = len(num)/2
    num.sort()
    if len(num) % 2 == 1:
        print(num[round(a)-1])
    else:
        print((num[round(a-1)]+num[round(a)])/2)
        #10, 10    9.10     
def mDeviation():
    c = []
    m = sum(num)/len(num)
    for a in range(len(num)):
        dev = num[a] - m
        c.append(dev)
    print(c)
    
def mVariance():
    c = []
    d = []
    m = sum(num)/len(num)
    for a in range(len(num)):
        dev = (num[a] - m) ** 2
        c.append(dev)
        d = sum(c) / (len(num)-1)
    print(d)
    
def mStandardDeviation():
    c= []
    d = []
    m = sum(num)/len(num)
    for a in range(len(num)):
        dev = (num[a] - m) ** 2
        c.append(dev)
        d = sum(c) / (len(num)-1)
    print(d)
    print(d**(1/2))
    
def mRange():
    print(max(num)-min(num))
    


# In[508]:


mMean()


# In[509]:


mMedian()


# In[510]:


mDeviation()


# In[511]:


mVariance()


# In[512]:


mStandardDeviation()


# In[513]:


mRange()

