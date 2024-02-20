#!/usr/bin/env python
# coding: utf-8

# In[2]:


from matplotlib import pyplot as plt
import pandas as pd


# In[4]:


data = {'year' : [2008,2009,2010],
        'atendees' : [112,321,729],
       'average age' : [19,23,31]}

df = pd.DataFrame(data)


# In[5]:


df


# In[7]:


earlier_than_2010 = df['year'] < 2010


# In[8]:


##Boolean Indexing


# In[9]:


df[earlier_than_2010]


# In[14]:


plt.plot(df['year'] , df['atendees'])
plt.plot(df['year'] , df['average age'])
plt.legend(['atendees', 'average age'])
plt.show()


# In[ ]:




