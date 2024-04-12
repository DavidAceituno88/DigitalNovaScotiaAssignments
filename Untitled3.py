#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
from datetime import datetime


# In[11]:


df = pd.read_excel('C:\\Users\\David\\Downloads\\Phase 3\\groundwrk_tbl.xlsx')


# In[12]:


df.head()


# In[91]:


df['date_clean'] = pd.to_datetime(df['Date'], errors='coerce')


# In[92]:


df.head()


# In[95]:


print(df.dtypes)


# In[101]:


def time_to_numeric(time_str):
    if isinstance(time_str, str):
        hours, minutes = map(int, time_str.split(':'))
        return hours * 60 + minutes
    elif np.isnan(time_str):  # Handle NaN values
        return 0  # or any other value you prefer for missing data
    else:
        return int(time_str)

# Convert the 'Hours' column to numeric
df['Hours'] = df['Hours'].apply(time_to_numeric)

sum_by_date = df.groupby('date_clean')['Hours'].sum()

print(sum_by_date)


# In[103]:


sum_by_date.plot(kind='bar')


# In[ ]:




