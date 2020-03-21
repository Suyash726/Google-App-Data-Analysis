#!/usr/bin/env python
# coding: utf-8

# # Import the required modules #
# 

# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# # Read Data #
# 

# In[12]:


google_data = pd.read_csv('D:\Repo\Data Analysis\googleplaystore.csv')


# In[13]:


google_data.head(10)


# In[59]:


google_data.shape


# In[17]:


#Now let us have a look at the Summary Statistics
google_data.describe()


# In[18]:


google_data.boxplot()
#We can observe that most of our data is concentrated on the range 2.5 to 5. We also have an outlier > 17.5.


# In[19]:


google_data.hist()


# In[20]:


google_data.info()
#Here it can be observed that there are a few Nan values possesed by Rating.


# # Data Cleaning #

# In[21]:


google_data.isnull()
#In the end we can see that there are a few true values which means there are a few null values in the rating column.


# In[22]:


google_data.isnull().sum()
#We can count the number of missing values in each column.


# In[23]:


google_data[google_data.Rating>5]
#Remember the one outlier we observed in the boxplot!


# In[24]:


google_data.drop(10472,inplace=True)


# In[26]:


google_data[10470:10476]
# The App has been removed!


# In[27]:


google_data.boxplot()


# In[28]:


google_data.hist()


# In[29]:


google_data.isnull().sum()


# # Data Manipulation and Imputation #

# ### We will be filling the missing values with mean, median or mode. #

# In[95]:


#This function fills the missing values with the median of the series.
def impute_median(series):
    return series.fillna(series.median)


# In[96]:


google_data['Rating'] = google_data['Rating'].transform(impute_median)


# In[97]:


google_data.isnull().sum()


# In[98]:


# modes of categorical values
print(google_data['Type'].mode())
print(google_data['Current Ver'].mode())
print(google_data['Android Ver'].mode())


# In[99]:


google_data['Type'].fillna(str(google_data['Type'].mode().values[0]),inplace=True)
google_data['Current Ver'].fillna(str(google_data['Current Ver'].mode().values[0]),inplace=True)
google_data['Android Ver'].fillna(str(google_data['Android Ver'].mode().values[0]),inplace=True)


# In[100]:


google_data.isnull().sum()


# In[109]:


#Now we will convert the Price,Ratings and Reviews to Numerical Values
google_data['Price'] = google_data['Price'].apply(lambda x: str(x).replace('$', '') if '$' in str(x) else str(x))
google_data['Price'] = google_data['Price'].apply(lambda x: float(x))
google_data['Reviews'] = pd.to_numeric(google_data['Reviews'], errors='coerce')


# In[102]:


google_data['Installs'] = google_data['Installs'].apply(lambda x: str(x).replace('+', '') if '+' in str(x) else str(x))
google_data['Installs'] = google_data['Installs'].apply(lambda x: str(x).replace(',', '') if ',' in str(x) else str(x))
google_data['Installs'] = google_data['Installs'].apply(lambda x: float(x))


# In[103]:


google_data.head(10)


# In[104]:


google_data.describe()
#Now we have four rows!!


# # Data Visualization #

# In[114]:


grp = google_data.groupby('Category')
x = grp['Installs'].agg(np.mean)
y = grp['Price'].agg(np.sum)
z = grp['Reviews'].agg(np.mean)
print(x)
print(y)
print(z)


# In[115]:


google_data['Rating'].dtype


# In[122]:


plt.figure(figsize=(12,5))
plt.plot(x, 'ro')
plt.xticks(rotation=90)
plt.show()


# In[74]:


plt.figure(figsize=(16,5))
plt.plot(y,'r--', color='b')
plt.xticks(rotation=90)
plt.title('Category wise Pricing')
plt.xlabel('Categories-->')
plt.ylabel('Prices-->')
plt.show()


# In[118]:


plt.figure(figsize=(16,5))
plt.plot(z,'g^', color='g')
plt.xticks(rotation=90)
plt.title('Category wise Reviews')
plt.xlabel('Categories-->')
plt.ylabel('Reviews-->')
plt.show()


# In[119]:


plt.figure(figsize=(12,5))
plt.plot(x, 'ro')
plt.xticks(rotation=90)
plt.show()


# In[121]:


plt.figure(figsize=(16,5))
plt.plot(x,'ro', color='r')
plt.xticks(rotation=90)
plt.title('Category wise Installs')
plt.xlabel('Categories-->')
plt.ylabel('Installs-->')
plt.show()


# In[ ]:




