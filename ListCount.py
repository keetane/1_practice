#!/usr/bin/env python
# coding: utf-8

# In[29]:


from pathlib import Path
import glob
import os
import subprocess
subprocess.run(['jupyter', 'nbconvert', '--to', 'python', 'List&Count.ipynb'])


# In[18]:


p = Path(".")


# In[19]:


list(p.glob("*"))


# In[20]:


list(p.glob("*.mp4"))


# In[24]:


glob.glob("*")


# In[25]:


glob.glob("/Users/keetane/Downloads/YouTube/*.mp4")


# In[26]:


path = os.getcwd()  
files = os.listdir(path)  
count = len(files)  
print(count) 


# In[27]:


len(glob.glob('*.mp4'))


# In[28]:


len(glob.glob('*.mp3'))


# In[32]:


get_ipython().system('jupyter nbconvert --to python List&Count.ipynb')


# In[ ]:




