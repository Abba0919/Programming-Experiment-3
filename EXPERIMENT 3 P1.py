#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#Load the corresponding .csv file into a data frame named cars using pandas
cars = pd.read_csv('cars.csv')
cars


# In[3]:


#Display the first five rows of the resulting cars
cars.head()


# In[4]:


#Display the last five rows of the resulting cars
cars.tail()


# In[ ]:




