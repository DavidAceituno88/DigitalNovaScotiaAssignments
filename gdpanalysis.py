#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
from matplotlib import pyplot as plt


# In[2]:


data = pd.read_csv('countries.csv')


# In[3]:


data.head()


# In[8]:


data.groupby(['country','continent']).mean()


# 

# In[10]:


mean_gdp_per_capita = data.groupby(['country','continent']).mean().gdpPerCapita


# In[34]:


top5 = mean_gdp_per_capita.sort_values(ascending = False).head()
top5


# In[13]:


#How has Canada's gdp Per-Person grow compared to the rest of the top 5 countries


# In[37]:


kuwait = data[data.country == 'Kuwait']
switzerland = data[data.country == 'Switzerland']
norway = data[data.country == 'Norway']
us = data[data.country == 'United States']

canada = data[data.country == 'Canada']
canada.head()


# In[23]:


plt.plot(canada.year,canada.gdpPerCapita)
plt.title('GDP Per Capita in Canada')
plt.show()


# In[32]:


plt.subplot(311)
plt.title('GDP Per Capita')
plt.plot(canada.year,canada.gdpPerCapita)

plt.subplot(312)
plt.title('GDP in Billions')
plt.plot(canada.year,canada.population * canada.gdpPerCapita / 10**9)

plt.subplot(313)
plt.title('Population in Millions')
plt.plot(canada.year,canada.population / 10**6)

plt.tight_layout()
plt.show()


# In[43]:


plt.plot(kuwait.year,kuwait.gdpPerCapita)
plt.plot(switzerland.year,switzerland.gdpPerCapita)
plt.plot(norway.year,norway.gdpPerCapita)
plt.plot(us.year,us.gdpPerCapita)
plt.plot(canada.year,canada.gdpPerCapita)
plt.legend(['Kuwait','Switzerland','Norway','United States','Canada'])
plt.title('GDP Per Capita in the top 5 GDP Countries')
plt.show()


# In[ ]:


