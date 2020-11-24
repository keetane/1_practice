#!/usr/bin/env python
# coding: utf-8

# In[1]:


Keyword = input("What's Up? \n Great > 1 \n not bad > 2 \n terrible... > 3 \n none of your business..! > other keys \n your answer > ")

if Keyword == "1":
    result = 'Do you have a good news today?'
elif Keyword == "2":
    result = "nice"
elif Keyword == "3":
    result = "have a mercy"
else : result = "Take it easy"

print(result)


# In[2]:


# !jupyter nbconvert --to python Greeting.ipynb


# In[ ]:




