#!/usr/bin/env python
# coding: utf-8

# In[25]:


import os
os.chdir('E:\\refined datasets\\')
l = os.listdir()


# In[26]:


file = open("Names.txt","w+")


# In[27]:


c=1
for i in l:
    if i != "Names.txt":
        file.write(str(c) + " : " + i + "\n")
        c+=1


# In[28]:


file.close()


# In[ ]:




