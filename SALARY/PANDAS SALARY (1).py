#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_csv(r"C:\Users\USER\Documents\project csvs\Salaries.csv")
df


# In[4]:


df.info()


# # DISPLAY TOP 10 ROWS ROWS OF THE DATA

# In[6]:


df.head(10)


# # DISPLAY THE BOTTOM 10 ROWS

# In[8]:


df.tail(10)


# # CHECK FOR NULLS

# In[11]:


df.isnull().sum()


# # DROP ID,NOTES,AGENCY AND STATUS COLUMNS

# In[14]:


df.columns


# In[16]:


df = df.drop(['Id','Notes','Status','Agency'],axis = 1)


# In[17]:


df.columns


# # GET THE OVERALL STATISTICS OF THE DATA

# In[20]:


df.describe()


# # FIND THE OCCURENCE OF EMPLOYEE NAMES (TOP 5)

# In[23]:


df.columns


# In[25]:


df['EmployeeName'].value_counts().head()


# # FIND THE NUMBER OF UNIQUE JOB TITLES

# In[26]:


df['JobTitle'].nunique()


# # TOTAL NUMBER OF JOB TITLES THAT CONTAIN CAPTAIN

# In[29]:


len(df[df['JobTitle'].str.contains('CAPTAIN',case= False)])


# # DISPLAY ALL EMPLOYEE NAMES FROM THE FIRE DEPARTMENT

# In[31]:


df[df['JobTitle'].str.contains('fire',case=False)]['EmployeeName']


# # FIND THE MINIMUM,MAXIMUM AND AVERAGE TOTAL PAY

# # MINIMUM

# In[55]:


df['TotalPay'].min()


# # MAXIMUM

# In[57]:


df['TotalPay'].max()


# # average

# In[58]:


df['TotalPay'].mean()


# # REPLACE 'NOT PROVIDED ' IN THE EMPLOYEE COLUMN WITH 'NAN'

# In[39]:


import numpy as np
df['EmployeeName'].replace('Not provided',np.nan)


# # DROP ROWS HAVING MORE THAN 5 MISSING VALUES

# In[45]:


df[df.isnull().sum(axis =1)==5]


# # FIND THE JOB TITLE OF ALBERT PARDONI

# In[48]:


df[df['EmployeeName']== 'ALBERT PARDINI']['JobTitle']


# # WHATS THE NAME OF THE PERSON WITH THE HIGHEST TOTAL PAY

# In[49]:


df[df['TotalPay'].max()==df['TotalPay']] 


# # FIND THE AVERAGE TOTAL PAY OF ALL EMPLOYEES PER YEAR

# In[51]:


df.groupby('Year').mean()['TotalPay']


# # FIND THE AVERAGE TOTAL PAY OF ALL EMPLOYEES PER JOB TITLE

# In[52]:


df.groupby('JobTitle').mean()['TotalPay']


# # FIND THE TOP 5 MOST COMMON JOB TITLES

# In[54]:


df['JobTitle'].value_counts().head()

