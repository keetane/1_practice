#!/usr/bin/env python
# coding: utf-8

# In[2]:


from pytube import YouTube
import os
import glob


# In[3]:


url = input("Enter the YouTube URL : ")
print("now downloading...")


# In[4]:


YouTube(url).streams.get_highest_resolution().download('/Users/keetane/Downloads/YouTube/movie')
YouTube(url).streams.get_audio_only().download('/Users/keetane/Downloads/YouTube/music')


# In[6]:


for name in glob.glob('/Users/keetane/Downloads/YouTube/music/*.mp4'):
    print('Downloaded file name is \n' + name)


# In[7]:


audioname = name.replace('.mp4', '.mp3')
audioname


# In[8]:


os.rename(name, audioname)


# In[9]:


print("fertig")


# In[ ]:




