#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
os.rename("old.txt", "new.txt")


# In[3]:


os.rename("/Users/ririretnaningtyas/python/riri/biology/old.txt", "/Users/ririretnaningtyas/python/riri/old.txt")


# In[4]:


os.rename("/Users/ririretnaningtyas/python/riri/old_folder", "/Users/ririretnaningtyas/python/riri/new_folder")


# In[5]:


os.mkdir("/Users/ririretnaningtyas/python/riri/chapt9")


# In[6]:


os.mkdirs("/Users/ririretnaningtyas/python/riri/biology/folders")


# In[7]:


shutil.copy("/Users/ririretnaningtyas/python/riri/original.txt", "/Users/ririretnaningtyas/python/riri/copy.txt")


# In[8]:


import shutil


# In[9]:


shutil.copy("/Users/ririretnaningtyas/python/riri/original.txt", "/Users/ririretnaningtyas/python/riri/copy.txt")


# In[10]:


shutil.copytree("/Users/ririretnaningtyas/python/riri/original_folder", "/Users/ririretnaningtyas/python/riri/copy_folder")


# In[12]:


os.path.exists("/Users/ririretnaningtyas/python/riri/email.txt")


# In[13]:


if os.path.exists("/Users/ririretnaningtyas/python/riri/email.txt")
    print("You have mail!")


# In[14]:


os.remove("/Users/ririretnaningtyas/python/riri/empty")


# In[15]:


os.remove("/Users/ririretnaningtyas/python/riri/unwanted_files")


# In[16]:


os.rmdir("/Users/ririretnaningtyas/python/riri/empty")


# In[17]:


shutil.rmtree("/Users/ririretnaningtyas/python/riri/full")


# In[19]:


os.listdir(".")


# In[20]:


os.listdir("/Users/ririretnaningtyas/python/riri")


# In[22]:


import subprocess
subprocess.call("/bin/date")


# In[23]:


import subprocess


# In[36]:


subprocess.call("/bin/date")


# In[37]:


subprocess.call("/bin/date/ +%B", shell=True)


# In[31]:


subprocess.call("/bin/date")


# In[33]:


current_month = subprocess.check_output("/bin/date +%B", shell=True)


# In[35]:


import re


# In[38]:


current_month.rstrip()


# In[39]:


dna = "ATCGATCGTGACTAGCTACCG"


# In[ ]:


accession = input("Enter the accession name")
# do something with the accession variable
print(accession)


# In[ ]:


accession.rstrip()


# In[ ]:


import sys
print(sys.argv)


# In[ ]:




