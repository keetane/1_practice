#!/usr/bin/env python
# coding: utf-8

# In[4]:


import glob
import os

path = "./test/"
list = os.listdir(path) # file = glob.glob(path + "*")と同じ

for file in list:
    if file != '.*':
        if os.path.isfile(os.path.join(path, file)):
            file = file
files_dir = [f for f in list if os.path.isdir(os.path.join(path, f))]
# file名のみの一覧を取得したい場合は、同じように、os.path.isfile()を使う。
print(file)


# In[ ]:





# In[42]:


kw = input("Enter the filename ")


# In[33]:


print(path + files)


# In[ ]:




