#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[26]:


import seaborn as sns
import matplotlib as plt


# # Import the first dataset

# In[2]:


df = pd.read_csv(r"C:\Users\USER\Documents\project csvs\employee_engagement_survey_data 1.csv")
df


# # Drop unwanted columns

# In[3]:


df.drop('Survey Date',axis=1,inplace=True)


# #  Check for nulls

# In[4]:


df.isnull().sum()


# In[5]:


df.info()


# In[6]:


df=df.astype(float)


# # Import the second dataset

# In[18]:


df1 = pd.read_csv(r"C:\Users\USER\Documents\project csvs\employee_data.csv")
df1


# # Drop columns that wont be used

# In[24]:


df1.drop(['StartDate','TerminationType','TerminationDescription','Supervisor'],axis=1,inplace=True)


# In[25]:


df1.info()


# #  1. Is there a correlation between satisfaction and worklife balance score

# In[17]:


df['Satisfaction Score'].corr(df['Work-Life Balance Score'])


# # 2. is there a correlation between work life balance and  and engagement score

# In[16]:


df['Work-Life Balance Score'].corr(df['Engagement Score'])


# # 3. Does the marital status  of one impact their current rating?

# In[27]:


sns.barplot(x='MaritalDesc', y= 'Current Employee Rating', data = df1)

