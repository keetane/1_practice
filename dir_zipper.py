#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import glob
import os
import shutil

path = "/work/1_practice/test/"
files = os.listdir(path) # file = glob.glob(path + "*")と同じ
files_dir = [f for f in files if os.path.isdir(os.path.join(path, f))]
# file名のみの一覧を取得したい場合は、同じように、os.path.isfile()を使う。
files_dir.sort()

# In[ ]:


KeyWord = input("Enter the Title Name")
KeyWordDirectory = path + KeyWord + "/"
os.makedirs(KeyWordDirectory)


# In[ ]:


for i, f in enumerate(files_dir):
    dname = kw + "{0:03d}".format(i+1)
    os.rename(path + f, path + dname)
    shutil.make_archive(path + dname, "zip", path + dname)
    zname = path + dname + ".zip"
    shutil.move(zname, KeyWordDirectory)
print("fertig")

