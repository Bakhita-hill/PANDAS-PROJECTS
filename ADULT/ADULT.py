#!/usr/bin/env python
# coding: utf-8

# In[50]:


import pandas as pd


# In[51]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[52]:


df = pd.read_csv(r"C:\Users\USER\Documents\project csvs\adult.csv")
df


# # Display top 10 rows

# In[6]:


df.head(10)


# # Check the last 10 rows of the dataset

# In[8]:


df.tail(10)


# # Find the shape of the dataset

# In[12]:


df.shape


# In[14]:


print ("number of rows",df.shape[0])
print ("number of columns",df.shape[1])


# # Get info about the dataset

# In[16]:


df.info()


# # Fetch random samples from the dataset 50%

# In[18]:


df.sample(frac=0.50)


# # check for null values

# In[21]:


df.isnull().sum()


# In[22]:


sns.heatmap(df.isnull())


# # replace '?' with nan

# In[54]:


df.isin(['?']).sum()


# In[55]:


import numpy as np


# In[56]:


df['workclass'] = df['workclass'].replace('?',np.nan)
df['occupation'] = df['occupation'].replace('?',np.nan)
df['native-country'] = df['native-country'].replace('?',np.nan)


# In[57]:


df.isin(['?']).sum()


# In[58]:


sns.heatmap(df.isnull())


# # drop missing values

# In[60]:


df.dropna(how='any',inplace=True)
df.shape


# # Check for duplicate data and drop them

# In[62]:


dup = df.duplicated().any()
print("is there any duplicated values in the data",dup)


# In[64]:


df=df.drop_duplicates()


# In[65]:


df.shape


# # get the overall statistics

# In[67]:


df.describe()


# # drop columns educational-num','capital-gain', 'capital-loss'

# In[69]:


df.columns


# In[71]:


df=df.drop(['educational-num','capital-gain', 'capital-loss'],axis = 1)


# In[72]:


df.columns


# # univariate analysis

# # what is the distribution of  the age column

# In[75]:


df['age'].describe()


# In[76]:


df['age'].hist()


# # find the total number of persons aged between 17$48 usung the between method

# In[78]:


sum(df['age'].between(17,48))


# # what is the distribution of the workplace column

# In[80]:


df['workclass'].describe()


# In[83]:


plt.figure(figsize=(10,10))
df['workclass'].hist()


# # how many people have bachelors degree or masters degree

# In[85]:


filter1= df['education']=='Bachelors'
filter2= df['education']=='Mastors'


# In[86]:


len(df[filter1 |filter2])


# # bivariate analysis

# In[89]:


df.columns


# In[90]:


sns.boxplot(x='income',y='age',data=df)


# # replace income values [<50k] and [>50k] with 0$1

# In[95]:


df.replace(to_replace= ['<=50K','>50K'],value=[0,1],inplace= True)


# In[96]:


df.head()


# # which workclass are getting the highest income

# In[99]:


df.groupby('workclass')['income'].mean().sort_values(ascending= False)


# # who has better chance to get incomr above 50k male or female

# In[101]:


df.groupby('gender')['income'].mean().sort_values(ascending= False)


# # convert the data type of work class to category

# In[103]:


df['workclass']=df['workclass'].astype('category')


# In[104]:


df.info()

