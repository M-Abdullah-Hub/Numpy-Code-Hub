#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


# In[5]:


Data=np.array([[101,111,112,113,141,115,116,117,118,119],[110,111,112,113,114,115,116,117,118,119],[110,111,121,131,141,151,611,711,811,119],[120,121,122,123,124,125,126,127,128,129]])


# In[6]:


type(Data)


# In[7]:


Data.shape


# In[8]:


np.__version__


# In[9]:


Data


# In[10]:


Data[2,5]


# In[11]:


Data.ndim


# In[12]:


Data2=np.array([101, 111, 112, 113, 141, 115, 116, 117, 118, 119],ndmin=1)              
Data2.ndim


# In[13]:


Data2[2]+Data2[9]


# In[14]:


np.arange(start=100,stop=205,step=5)


# In[15]:


np.arange(5,100,5)


# In[16]:


np.arange(10)


# In[17]:


np.arange(-19,2)


# In[18]:


X=np.arange(1)
print(X.dtype)


# In[19]:


np.sin(Data2)


# # Plot() Numpy

# In[23]:


import numpy as np
import matplotlib.pyplot as plt


# In[24]:


Array=np.array([1,2,3,4,5,9,8,7,6,5])
Array


# In[25]:


plt.plot(Array)  
plt.show()


# In[ ]:





# In[ ]:




