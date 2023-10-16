#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


df = pd.read_csv(r"C:\Users\USER\Documents\project csvs\diabetes.csv")
df


# # What are the total number of records in the dataset?
# 

# In[8]:


df.info()


# In[7]:


df = df.astype(float)


# # What is the average age of the patients in the dataset?

# In[10]:


df['Age'].mean ()


# # What is the maximum and minimum BMI (Body Mass Index) in the dataset?

# In[11]:


df['BMI'].max()


# In[12]:


df['BMI'].min()


# # What is the average glucose level in the dataset?

# In[15]:


df['Glucose'].mean()


# # How many patients in the dataset have been diagnosed with diabetes (Outcome = 1)?

# In[17]:


diabetic_patients = len(df[df['Outcome']== 1])
diabetic_patients


# # What percentage of patients have diabetes?

# In[25]:


total = len(df['Outcome'])
total


# In[26]:


(diabetic_patients / total)* 100


# # How many patients with diabetes have a BMI greater than 30?

# In[28]:


len(df[df['Outcome']== 1]) & len(df[df['BMI']>= 30])


# # How many patients fall into each age group (e.g., 20-30, 30-40, etc.)?

# In[35]:


age_bins = [20, 30, 40, 50, 60, 70, 80]
age_groups = pd.cut(df['Age'], bins=age_bins)
age_group_counts = age_groups.value_counts()
print(age_group_counts)


# # What is the average BMI for patients in different age groups?

# In[37]:


avg_bmi_by_age_group = df.groupby(age_groups)['BMI'].mean()
avg_bmi_by_age_group


# # Is there a correlation between age and glucose level?

# In[38]:


correlation_age_glucose = df['Age'].corr(df['Glucose'])
correlation_age_glucose 


# # Is there a correlation between BMI and blood pressure

# In[41]:


df['BMI'].corr(df['BloodPressure'])


# # What is the correlation coefficient between BMI and skin thickness?

# In[42]:


df['BMI'].corr(df['SkinThickness'])


# # is there a correlateion of the outcome and pregnancies

# In[43]:


df['Outcome'].corr(df['Pregnancies'])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




