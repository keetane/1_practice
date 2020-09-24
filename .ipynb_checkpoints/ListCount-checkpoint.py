#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pathlib import Path
import glob
import os


# In[2]:


p = Path(".")


# In[3]:


list(p.glob("*"))


# In[5]:


Lmp4 = list(p.glob("*.mp4"))
list(p.glob("*.mp4"))


# In[6]:


glob.glob("*")


# In[8]:


lmp4 = glob.glob("/Users/keetane/Downloads/YouTube/movie/*.mp4")


# In[14]:


path = os.getcwd()  
files = os.listdir(path)  
count = len(files)  
print("the number of files in this directory is " + str(count))


# In[12]:


nmp4 = len(glob.glob('./movei/*.mp4'))
nmp3 = len(glob.glob('./music/*.mp3'))
len(glob.glob('*.mp4'))
len(glob.glob('*.mp3'))


# In[13]:


print('number of mp4 file is ' + str(nmp4))
print('number of mp3 file is ' + str(nmp3))


# In[ ]:




