#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[7]:


cars = pd.read_csv('cars.csv')
cars


# In[23]:


#Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
cars[1::2].head()


# In[43]:


#Display the row that contains the Model of Mazda RX4
cars.loc[cars['Model']=='Mazda RX4']


# In[45]:


#Display how many cylinders does Camaro Z28 have
cars.loc[[23],['Model', 'cyl']]


# In[49]:


#Display how many cylinders and gears does the 3 models have
cars.loc[[1, 28, 18],['Model', 'cyl', 'gear']]


# In[ ]:




