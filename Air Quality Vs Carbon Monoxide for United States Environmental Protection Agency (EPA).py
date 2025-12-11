#!/usr/bin/env python
# coding: utf-8

# In[1]:


##Explore descriptive statistics


# In[2]:


# Import relevant Python libraries.

import pandas as pd
import numpy as np


# In[3]:


# Load data from the .csv file into a DataFrame and save in a variable.

epa_data = pd.read_csv("c4_epa_air_quality.csv", index_col = 0)


# In[4]:


# Display first 10 rows of the data.

epa_data.head(10)


# In[5]:


#The aqi column represents the EPA's Air Quality Index (AQI).
# Get descriptive stats.

epa_data.describe()


# In[6]:


# Intial Findings

#The count value for the aqi column is 260. This means there are 260 aqi measurements represented in this dataset.

#The 25th percentile for the aqi column is 2. This means that 25% of the aqi values in the data are below 2.

#The 75th percentile for the aqi column is 9. This means that 75% of the aqi values in the data are below 9.


# In[7]:


# Get descriptive stats about the states in the data.

epa_data["state_name"].describe()


# In[8]:


# There are 260 state values, and 52 of them are unique. California is the most commonly occurring state in the data, with a frequency of 66. (In other words, 66 entries in the data correspond to aqi measurements taken in California.)


# In[9]:


# Compute the mean value from the aqi column.

np.mean(epa_data["aqi"])


# In[10]:


# The mean value for the aqi column is approximately 6.76 (rounding to 2 decimal places here). This means that the average aqi from the data is approximately 6.76.


# In[11]:


# Compute the median value from the aqi column.

np.median(epa_data["aqi"])


# In[12]:


# The median value for the aqi column is 5.0. This means that half of the aqi values in the data are below 5.


# In[14]:


# Identify the minimum value from the aqi column.

np.min(epa_data["aqi"])


# In[15]:


# Identify the maximum value from the aqi column.

np.max(epa_data["aqi"])


# In[16]:


# The minimum value for the aqi column is 0. This means that the smallest aqi value in the data is 0.
# The maximum value for the aqi column is 50. This means that the largest aqi value in the data is 50.


# In[17]:


# Compute the standard deviation for the aqi column.

np.std(epa_data["aqi"], ddof=1)


# In[18]:


# The standard deviation for the aqi column is approximately 7.05 (rounding to 2 decimal places here). This is a measure of how spread out the aqi values are in the data.


# In[19]:


# "AQI values at or below 100 are generally thought of as satisfactory. When AQI values are above 100, air quality is considered to be unhealthy—at first for certain sensitive groups of people, then for everyone as AQI values increase."
# "An AQI of 100 for carbon monoxide corresponds to a level of 9.4 parts per million."
# The average AQI value in the data is approximately 6.76, which is considered safe with respect to carbon monoxide. Further, 75% of the AQI values are below 9.


# In[ ]:




