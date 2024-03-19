#!/usr/bin/env python
# coding: utf-8

# In[10]:


import urllib3
from bs4 import BeautifulSoup
import requests


# In[7]:


articleURL = "https://jitsmagazine.com/three-adcc-veterans-set-to-return-at-adcc-2024/" 


# In[11]:


response = requests.get(articleURL)
soup = BeautifulSoup(response.content, "html.parser")
soup


# In[34]:


text = soup.find('div', {"class": "jeg_main_content"}).text
text


# In[47]:


text.strip()


# In[ ]:




