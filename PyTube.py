#!/usr/bin/env python
# coding: utf-8

# In[116]:


from pytube import YouTube
import os
import glob


# In[122]:


url = input("Enter the YouTube URL : ")
print("now downloading...")


# In[123]:


YouTube(url).streams.get_highest_resolution().download('/Users/keetane/Downloads/YouTube/movie')
YouTube(url).streams.get_audio_only().download('/Users/keetane/Downloads/YouTube/music')


# In[139]:


for name in glob.glob('/Users/keetane/Downloads/YouTube/music/*.mp4'):
    audioname


# In[140]:


audioname = name.replace('.mp4', '.mp3')
audioname


# In[141]:


os.rename(name, audioname)


# In[ ]:


print("fertig")

