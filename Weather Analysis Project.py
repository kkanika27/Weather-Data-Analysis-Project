#!/usr/bin/env python
# coding: utf-8

# ## The Weather Dataset

# The Weather Dataset is the time series data set with per hour information about the weather conditions at a particular location. It records Temperature, Dew-point Temperature, Relative Humidity, Wind Speed, Visibility, Pressure and Conditions.
# 
# This data is available as a CSV file. We are going to analyze this data set using the Pandas Dataframe.

# In[1]:


import pandas as pd


# In[4]:


data = pd.read_csv("WeatherData.csv")


# In[5]:


data


# ## Analyzing the Data

# In[6]:


data.head()
#displays top 5 rows


# In[8]:


data.shape
#shows total no. of rows and columns


# In[9]:


data.index
#displays the index of the dataframe


# In[10]:


data.columns
#displays column names


# In[11]:


data.dtypes
#displays data-type of each column


# In[15]:


data['Weather'].unique()
#displays unique values in a column


# In[16]:


data.nunique()
#displays total unique values in each column


# In[17]:


data.count()
#displays total non-null values in each column


# In[19]:


data['Weather'].value_counts()
#displays all unique values with their count in the column


# In[20]:


data.info()
#provides basic information about the dataset


# ### Find all the unique "Wind Speed" values in the data.

# In[21]:


data.head()


# In[27]:


data['Wind Speed_km/h'].unique()


# ### Find the number of times when the 'Weather is exactly Clear'. 

# In[29]:


data[data['Weather']== 'Clear']
#filtered data 


# ### Find the number of times when the "Wind speed was exactly 4 km/h".

# In[30]:


data[data["Wind Speed_km/h"]==4]
#filtered data


# ### Find out all the null values in the data

# In[31]:


data.isnull().sum()
#display null values for each column


# ### Rename the column name 'Weather' of the dataframe to 'Weather Condition'

# In[32]:


data.rename(columns = {'Weather': 'Weather Condition'}, inplace = True)


# In[33]:


data.head()


# ### What is the mean 'Visibility'?

# In[36]:


data['Visibility_km'].mean()


# ### What is the Standard Deviation of 'Pressure' in this data?

# In[38]:


data['Press_kPa'].std()


# ### What is the variance of 'Relative Humidity' in this data?

# In[39]:


data['Rel Hum_%'].var()


# ### Find all the instances when snow was recorded.

# In[43]:


data[data["Weather Condition"] == "Snow"]


# ### Find all the instances when 'Wind Speed is above 24' and 'Visibility is 25'

# In[44]:


data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]
#display data when 'Wind Speed is above 24' and 'Visibility is 25'


# ### What is the mean value of each column against each 'Weather Condition'?

# In[45]:


data.groupby('Weather Condition').mean()


# ### What is the Minimum and Maximum value of each column against each 'Weather Condition'?

# In[46]:


data.groupby('Weather Condition').min()


# In[47]:


data.groupby('Weather Condition').max()


# ### Show all the Records where the Weather Condition is Fog.

# In[48]:


data[data['Weather Condition'] == "Fog"]


# ### Find all instances when "Weather is Clear" or "Visibility is above 40".

# In[51]:


data[(data['Weather Condition'] == "Clear") | (data['Visibility_km'] > 40)]


# ### Find all instances when:
# 
# A. 'Weather is Clear' and 'Relative Humidity is greater than 50' 
# 
# or
# 
# B. 'Visibility is above 40'

# In[52]:


data[(data['Weather Condition'] == "Clear") & (data['Rel Hum_%'] > 50) | (data['Visibility_km'] > 40)]

